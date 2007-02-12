# TODO
# - everything
Summary:	Graph performance data retrieved from Nagios using rrdtool
Summary(pl.UTF-8):	Rysowanie wykresów danych wydajności uzyskanych z Nagiosa przy użyciu rrdtoola
Name:		nagios-mypan
Version:	0.beta1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/mypan/mypan.beta.tar.gz
# Source0-md5:	58af8b3ec5ab0d06a160a907c980ce6d
URL:		http://sourceforge.net/projects/mypan/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mypan (MY Performance Add-on for Nagios) is as the name states an
add-on for Nagios. The goal is to provide an easy way to graph
performance data retrieved from Nagios using rrdtool.

%description -l pl.UTF-8
mypan (MY Performance Add-on for Nagios), jak sama nazwa wskazuje,
jest dodatkiem dla Nagiosa. Jego celem jest umożliwienie łatwego
tworzenia wykresów z danych dotyczących wydajności uzyskanych z
Nagiosa przy użyciu rrdtoola.

%prep
%setup -q -n mypan

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LEGAL README
TODO
