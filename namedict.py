'''
	ArcherC7v1_tp_recovery.bin
	ArcherC7v2_tp_recovery.bin
	ArcherC2600_1.0_tp_recovery.bin
	
'''

firmware_dict = {
	'buffalo-wzr-600dhp.bin':'',
	'buffalo-wzr-hp-ag300h.bin':'',
	'buffalo-wzr-hp-g300nh.bin':'',
	'buffalo-wzr-hp-g450h.bin':'',
	'd-link-dir-505-rev-a1.bin':'',
	'd-link-dir-615-rev-c1.bin':'',
	'd-link-dir-825-rev-b1.bin':'',
	'gl-inet-6408a-v1.bin':'',
	'gl-inet-6416a-v1.bin':'',
	'linksys-wrt160nl.bin':'',
	'netgear-wndr3700.img':'',
	'netgear-wndr3700v2.img':'',
	'netgear-wndr3700v4.img':'',
	'netgear-wndr3800.img':'',
	'netgear-wndr4300.img':'',
	'netgear-wndrmacv2.img':'',
	'onion-omega.bin':'',
	'tp-link-cpe210-v1.0.bin':'',
	'tp-link-cpe210-v1.1.bin':'',
	'tp-link-cpe220-v1.0.bin':'',
	'tp-link-cpe220-v1.1.bin':'',
	'tp-link-cpe510-v1.0.bin':'',
	'tp-link-cpe510-v1.1.bin':'',
	'tp-link-cpe520-v1.0.bin':'',
	'tp-link-cpe520-v1.1.bin':'',
	'tp-link-tl-mr13u-v1.bin':'',
	'tp-link-tl-mr3020-v1.bin':'',
	'tp-link-tl-mr3040-v1.bin':'',
	'tp-link-tl-mr3040-v2.bin':'',
	'tp-link-tl-mr3220-v1.bin':'',
	'tp-link-tl-mr3220-v2.bin':'',
	'tp-link-tl-mr3420-v1.bin':'mr3420v1_tp_recovery.bin',
	'tp-link-tl-mr3420-v2.bin':'mr3420v2_tp_recovery.bin',
	'tp-link-tl-wa701n-nd-v1.bin':'',
	'tp-link-tl-wa701n-nd-v2.bin':'',
	'tp-link-tl-wa750re-v1.bin':'',
	'tp-link-tl-wa801n-nd-v1.bin':'',
	'tp-link-tl-wa801n-nd-v2.bin':'',
	'tp-link-tl-wa830re-v1.bin':'',
	'tp-link-tl-wa830re-v2.bin':'',
	'tp-link-tl-wa850re-v1.bin':'',
	'tp-link-tl-wa860re-v1.bin':'',
	'tp-link-tl-wa901n-nd-v1.bin':'',
	'tp-link-tl-wa901n-nd-v2.bin':'',
	'tp-link-tl-wa901n-nd-v3.bin':'',
	'tp-link-tl-wdr3500-v1.bin':'',
	'tp-link-tl-wdr3600-v1.bin':'',
	'tp-link-tl-wdr4300-v1.bin':'wdr4300v1_tp_recovery.bin',
	'tp-link-tl-wdr4900-v1.bin':'',
	'tp-link-tl-wr1043n-nd-v1.bin':'wr1043nv1_tp_recovery.bin',
	'tp-link-tl-wr1043n-nd-v2.bin':'wr1043nv2_tp_recovery.bin',
	'tp-link-tl-wr1043n-nd-v3.bin':'wr1043nv3_tp_recovery.bin',
	'tp-link-tl-wr2543n-nd-v1.bin':'',
	'tp-link-tl-wr703n-v1.bin':'',
	'tp-link-tl-wr710n-v1.bin':'',
	'tp-link-tl-wr710n-v2.bin':'',
	'tp-link-tl-wr740n-nd-v1.bin':'',
	'tp-link-tl-wr740n-nd-v3.bin':'',
	'tp-link-tl-wr740n-nd-v4.bin':'',
	'tp-link-tl-wr740n-nd-v5.bin':'',
	'tp-link-tl-wr741n-nd-v1.bin':'',
	'tp-link-tl-wr741n-nd-v2.bin':'',
	'tp-link-tl-wr741n-nd-v4.bin':'',
	'tp-link-tl-wr741n-nd-v5.bin':'',
	'tp-link-tl-wr743n-nd-v1.bin':'',
	'tp-link-tl-wr743n-nd-v2.bin':'',
	'tp-link-tl-wr841n-nd-v10.bin':'wr841nv10_tp_recovery.bin',
	'tp-link-tl-wr841n-nd-v11.bin':'wr841nv11_tp_recovery.bin',
	'tp-link-tl-wr841n-nd-v3.bin':'',
	'tp-link-tl-wr841n-nd-v5.bin':'',
	'tp-link-tl-wr841n-nd-v7.bin':'',
	'tp-link-tl-wr841n-nd-v8.bin':'mr3420v2_tp_recovery.bin',
	'tp-link-tl-wr841n-nd-v9.bin':'wr841nv9_tp_recovery.bin',
	'tp-link-tl-wr842n-nd-v1.bin':'wr842ndv1_tp_recovery.bin',
	'tp-link-tl-wr842n-nd-v2.bin':'wr842ndv2_tp_recovery.bin',
	'tp-link-tl-wr843n-nd-v1.bin':'',
	'tp-link-tl-wr940n-nd-v1.bin':'',
	'tp-link-tl-wr940n-nd-v2.bin':'',
	'tp-link-tl-wr940n-nd-v3.bin':'',
	'tp-link-tl-wr941n-nd-v2.bin':'',
	'tp-link-tl-wr941n-nd-v3.bin':'',
	'tp-link-tl-wr941n-nd-v4.bin':'',
	'tp-link-tl-wr941n-nd-v5.bin':'',
	'tp-link-tl-wr941n-nd-v6.bin':'',
	'ubiquiti-airgateway.bin':'',
	'ubiquiti-airrouter.bin':'',
	'ubiquiti-bullet-m.bin':'',
	'ubiquiti-loco-m-xw.bin':'',
	'ubiquiti-loco-m.bin':'',
	'ubiquiti-nanostation-m-xw.bin':'',
	'ubiquiti-nanostation-m.bin':'',
	'ubiquiti-picostation-m.bin':'',
	'ubiquiti-rocket-m.bin':'',
	'ubiquiti-unifi-ap-pro.bin':'',
	'ubiquiti-unifi.bin':'',
	'ubiquiti-unifiap-outdoor+.bin':'',
	'ubiquiti-unifiap-outdoor.bin':'',
	'wd-my-net-n600.bin':'',
	'wd-my-net-n750.bin':'',
	'x86-64-virtualbox.vdi':'',
	'x86-64-vmware.vmdk':'',
	'x86-64.img.gz':'',
	'x86-generic.img.gz':'',
	'x86-kvm.img.gz':'',
	'x86-virtualbox.vdi':'',
	'x86-vmware.vmdk':'',
	'x86-xen.img.gz':'',
}
