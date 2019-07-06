BUILD_DIR=build
SRC_DIR=website

.PHONY: $(BUILD_DIR)

$(BUILD_DIR):
	rm -rf $(BUILD_DIR)/* && \
	cp -r ${SRC_DIR}/* build && \
	python3 build.py $(BUILD_DIR)
