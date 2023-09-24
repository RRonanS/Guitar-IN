#include <linux/module.h>
#include <linux/init.h>
#include <linux/usb.h>
#include <linux/proc_fs.h>

/* Meta Information */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("RRonan");
MODULE_DESCRIPTION("Driver para entrada de guitarra");

#define VENDOR_ID 0x0d8c
#define PRODUCT_ID 0x000c

static struct proc_dir_entry *proc_file;
static struct usb_device *usb_dev;

// Lê os dados do arquivo proc
static ssize_t my_read(struct file *File, char *user_buffer, size_t count, loff_t *offs) {
	char text[] = "OLá mundo!\n";
	int to_copy, not_copied, delta;

	/* Get amount of data to copy */
	to_copy = min(count, sizeof(text));

	/* Copy data to user */
	not_copied = copy_to_user(user_buffer, text, to_copy);

	/* Calculate data */
	delta = to_copy - not_copied;

	return delta;
}

// Escreve no arquivo proc
static ssize_t my_write(struct file *File, const char *user_buffer, size_t count, loff_t *offs) {
	char text[255];
	int to_copy, not_copied, delta;

	/* Clear text */
	memset(text, 0, sizeof(text));

	/* Get amount of data to copy */
	to_copy = min(count, sizeof(text));

	/* Copy data to user */
	not_copied = copy_from_user(text, user_buffer, to_copy);
	//printk("guitarin- escrito %s no arquivo\n", text);

	/* Calculate data */
	delta = to_copy - not_copied;

	return delta;
}

// Estrutura para gerenciar a leitura e escrita no arquivo proc
static struct proc_ops fops = {
	.proc_read = my_read,
	.proc_write = my_write,
};

// Tabela de dispositivos usb
static struct usb_device_id usb_dev_table [] = {
	{ USB_DEVICE(VENDOR_ID, PRODUCT_ID) },
	{},
};
MODULE_DEVICE_TABLE(usb, usb_dev_table);

// Funcao chamada quando o dispositivo é conectado
static int my_usb_probe(struct usb_interface *intf, const struct usb_device_id *id) {
	printk("guitarin - Dispositivo detectado\n");
	
	usb_dev = interface_to_usbdev(intf);
	if(usb_dev == NULL) {
		printk("guitarin - Dispositivo nao encontrado\n");
		return -1;
	}

	proc_file = proc_create("guitarin", 0666, NULL, &fops);
	if(proc_file == NULL) {
		printk("guitarin - Erro ao criar /proc/guitarin\n");
		return -ENOMEM;
	}

	return 0;
}

// Funcao chamada quando o dispositivo usb se desconecta
static void my_usb_disconnect(struct usb_interface *intf) {
	proc_remove(proc_file);
	printk("guitarin - Dispositivo desconectado\n");
}

// Estrutura para as funcoes do driver
static struct usb_driver my_usb_driver = {
	.name = "guitarin",
	.id_table = usb_dev_table,
	.probe = my_usb_probe,
	.disconnect = my_usb_disconnect,
};

// Inicializando driver
static int __init my_init(void) {
	int result;
	printk("guitarin- Inicializando\n");
	result = usb_register(&my_usb_driver);
	if(result) {
		printk("guitarin - Problema na inicializacao\n");
		return -result;
	}

	return 0;
}

// Ao desativar o driver
static void __exit my_exit(void) {
	printk("guitarin- Saindo\n");
	usb_deregister(&my_usb_driver);
}

module_init(my_init);
module_exit(my_exit);
