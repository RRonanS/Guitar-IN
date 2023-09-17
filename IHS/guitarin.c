#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/usb.h>

MODULE_LICENSE("GPL");

static int captura_func(struct usb_interface *intf, const struct usb_device_id *id)
{
    // Logica para capturar sinais do Irig
    return 0;
}

static void disconectar_func(struct usb_interface *intf)
{
    // Liberacao dos recursos
}

static const struct usb_device_id tabela_mapeamento[] = {
    // Entradas da tabela
    //{ USB_DEVICE(VENDOR_ID, PRODUCT_ID) },
};

static struct usb_driver seu_driver = {
    .name = "guitar input",
    .probe = captura_func,
    .disconnect = disconectar_func,
    .id_table = tabela_mapeamento,
};

module_usb_driver(seu_driver);
