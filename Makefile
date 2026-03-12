.PHONY: help clean build publish \
        bump bump-patch bump-minor bump-major \
        release-patch release-minor release-major \
        show-version show-version-full \
        git-clean require-token require-remote push-release

# --------------------------------------------------------------------
# Load local environment variables if present (do NOT commit .env)
# --------------------------------------------------------------------
ifneq (,$(wildcard .env))
  include .env
  export
endif

# --------------------------------------------------------------------
# Version helpers
# --------------------------------------------------------------------
UV_VERSION_CMD = uv version
UV_VERSION_NUM_CMD = uv version | awk '{print $$NF}'

# Expected env var (loaded from .env):
# - UV_PUBLISH_TOKEN
# --------------------------------------------------------------------

help:
	@echo "Targets:"
	@echo "  make build           Build wheel + sdist into dist/"
	@echo "  make publish         Publish to PyPI (requires UV_PUBLISH_TOKEN)"
	@echo "  make bump-patch      Bump patch version"
	@echo "  make bump-minor      Bump minor version"
	@echo "  make bump-major      Bump major version"
	@echo "  make release-patch   Bump patch, commit, tag, push"
	@echo "  make release-minor   Bump minor, commit, tag, push"
	@echo "  make release-major   Bump major, commit, tag, push"
	@echo "  make show-version    Show version number"
	@echo "  make clean           Remove build artifacts"

# --------------------------------------------------------------------
# Safety checks
# --------------------------------------------------------------------
git-clean:
	@git diff --quiet && git diff --cached --quiet || \
	 (echo "ERROR: git working tree is not clean"; exit 1)

require-token:
	@test -n "$$UV_PUBLISH_TOKEN" || \
	 (echo "ERROR: UV_PUBLISH_TOKEN missing (check .env)"; exit 1)

require-remote:
	@git remote get-url origin >/dev/null 2>&1 || \
	 (echo "ERROR: remote 'origin' not configured"; exit 1)
	@git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1 || \
	 (echo "ERROR: no upstream branch set. Run: git push -u origin $$(git branch --show-current)"; exit 1)

push-release: require-remote
	@git push
	@git push --tags

# --------------------------------------------------------------------
# Version bumping
# --------------------------------------------------------------------
bump: bump-patch

bump-patch:
	uv version --bump patch

bump-minor:
	uv version --bump minor

bump-major:
	uv version --bump major

show-version:
	@$(UV_VERSION_NUM_CMD)

show-version-full:
	@$(UV_VERSION_CMD)

# --------------------------------------------------------------------
# Build / clean
# --------------------------------------------------------------------
clean:
	rm -rf dist build

build: clean
	uv build

# --------------------------------------------------------------------
# Publish (LOCAL ONLY, token via .env)
# --------------------------------------------------------------------
publish: build require-token
	uv publish --token "$$UV_PUBLISH_TOKEN"

# --------------------------------------------------------------------
# Release targets
# bump -> commit -> tag -> push
# Publishing remains explicit: `make publish`
# --------------------------------------------------------------------
release-patch: git-clean bump-patch
	@ver=$$($(UV_VERSION_NUM_CMD)) && full=$$($(UV_VERSION_CMD)) && \
	git commit -am "Release $$full" && \
	git rev-parse "v$$ver" >/dev/null 2>&1 && \
	 (echo "ERROR: tag v$$ver already exists"; exit 1) || true && \
	git tag "v$$ver"
	@$(MAKE) push-release

release-minor: git-clean bump-minor
	@ver=$$($(UV_VERSION_NUM_CMD)) && full=$$($(UV_VERSION_CMD)) && \
	git commit -am "Release $$full" && \
	git rev-parse "v$$ver" >/dev/null 2>&1 && \
	 (echo "ERROR: tag v$$ver already exists"; exit 1) || true && \
	git tag "v$$ver"
	@$(MAKE) push-release

release-major: git-clean bump-major
	@ver=$$($(UV_VERSION_NUM_CMD)) && full=$$($(UV_VERSION_CMD)) && \
	git commit -am "Release $$full" && \
	git rev-parse "v$$ver" >/dev/null 2>&1 && \
	 (echo "ERROR: tag v$$ver already exists"; exit 1) || true && \
	git tag "v$$ver"
	@$(MAKE) push-release