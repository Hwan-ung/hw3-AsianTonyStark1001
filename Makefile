ENV_NAME = myst-site
ENV_FILE = environment.yml
.PHONY: env html clean
env:
	@if conda env list | grep -q "^$(ENV_NAME) "; then \
		echo "Updating existing conda env: $(ENV_NAME) from $(ENV_FILE)"; \
		conda env update -n $(ENV_NAME) -f $(ENV_FILE) --prune; \
	else \
		echo "Creating conda env: $(ENV_NAME) from $(ENV_FILE)"; \
		conda env create -n $(ENV_NAME) -f $(ENV_FILE); \
	fi
	@echo "To use it: conda activate $(ENV_NAME)"
html:
	myst build --html
clean:
	@echo "Cleaning generated assets..."
	@rm -rf figures audio _build
