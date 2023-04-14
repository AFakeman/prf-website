BUILD_DIR=build
SRC_DIR=website

.PHONY: build_html

build_html: $(BUILD_DIR)
	rm -rf $(BUILD_DIR)/* && \
	cp -r ${SRC_DIR}/* build && \
	python3 build.py $(BUILD_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.PHONY:
deploy: build_html
	firebase deploy
