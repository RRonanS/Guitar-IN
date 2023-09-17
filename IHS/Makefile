obj-m += guitarin.o

all:
	@mkdir -p output
	@make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
	@mv *.ko *.o *.mod.c Module.symvers modules.order output/

clean:
	@make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
	@rm -rf output
