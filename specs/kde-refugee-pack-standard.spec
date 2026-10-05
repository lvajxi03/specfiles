Name:           kde-refugee-pack-standard
Version:        0.0.2
Release:        1%{?dist}
Summary:        KDE refugee pack, standard version

License:        MIT
BuildArch:	noarch

Requires:	kde-refugee-pack-minimal = 0.0.2
Requires:	blueman
Requires:	brightnessctl
Requires:	dunst
Requires:	flameshot
Requires:	lxqt-policykit
Requires:	network-manager-applet
Requires:	pavucontrol
Requires:	picom
Requires:	playerctl
Requires:	udiskie
Requires:	volumeicon
Requires:	qterminal
Requires:	stalonetray

%description
Mandatory metapackage for everyone who leaves KDE for fvwm3
(standard version)

%files

%changelog
* Sat Oct 03 2026 Marcin Bielewicz <marcin.bielewicz@gmail.com>
- initial version
