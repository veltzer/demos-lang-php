.PHONY: all
all: tools.stamp

tools.stamp:
	$(info doing [$@])
	@templar_cmd install_deps
	@make_helper touch-mkdir $@
