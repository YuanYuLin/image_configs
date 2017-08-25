import ops
import iopc

pkg_path = ""
output_dir = ""

def set_global(args):
    global pkg_path
    global output_dir 
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.copyto(ops.path_join(pkg_path, "fstab"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "nsswitch.conf"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "interfaces"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "passwd"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "dropbear/rsa.key"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "dropbear/authorized_keys"), output_dir)
    ops.copyto(ops.path_join(pkg_path, "X11/xorg.conf"), output_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return True

def MAIN_BUILD(args):
    set_global(args)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "fstab"), "etc")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "nsswitch.conf"), "etc")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "passwd"), "etc")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "interfaces"), "etc/network")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "authorized_keys"), "etc/dropbear")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "rsa.key"), "etc/dropbear")
    #iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "xorg.conf"), "etc/X11")
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

