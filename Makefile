.PHONY: build
build:
	nuitka --standalone --onefile --python-flag="-O,-m" --clang --remove-output src

.PHONY: run
run:
	./src.bin