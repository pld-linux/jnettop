Summary:	Network traffic tracker
Summary(pl):	Narzêdzie do ¶ledzenia ruchu sieciowego
Name:		jnettop
Version:	0.9
Release:	1
License:	GPL
Group:		Network/Monitoring
Source0:	http://jnettop.kubs.info/dist/%{name}-%{version}.tar.gz
# Source0-md5:	33ff9857b577c8d226639f55bb5cd69e
URL:		http://jnettop.kubs.info/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nettop is visualising active network traffic as top does with processes.
It displays active network streams sorted by bandwidth used. This is
often usable when you want to get a fast grip of what is going on on your
outbound router.

%description -l pl
Nettop pokazuje aktywny ruch sieciowy podobnie jak top procesy. Wy¶wietla
aktywne sieciowe strumienie posortowane wg ilo¶ci u¿ytego pasma. Jest czêsto
u¿ywany do stwierdzenia co siê dzieje na ruterach.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README .jnettop
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
