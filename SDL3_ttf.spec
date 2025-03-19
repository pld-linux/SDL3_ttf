Summary:	Simple DirectMedia Layer 3 - ttf handling
Summary(pl.UTF-8):	Biblioteka obsługi fontów TTF dla SDL3
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer 3 - Biblioteca de fontes TrueType
Name:		SDL3_ttf
Version:	3.2.0
Release:	1
License:	Zlib-like
Group:		Libraries
#Source0Download: https://github.com/libsdl-org/SDL_ttf/releases
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL3_ttf-%{version}.tar.gz
# Source0-md5:	3df1b42948bfa873e678923f380082a4
URL:		https://github.com/libsdl-org/SDL_ttf
BuildRequires:	OpenGL-devel
BuildRequires:	SDL3-devel >= 3.2.6
BuildRequires:	cmake >= 3.16
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	harfbuzz-devel >= 2.3.1
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	plutosvg-devel
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	SDL3 >= 3.2.6
Requires:	freetype >= 2.1.4
Requires:	harfbuzz >= 2.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to use TrueType fonts in
your SDL3 applications. It comes with an example program "sdl2font"
which displays an example string for a given TrueType font file.

%description -l pl.UTF-8
Przykładowa biblioteka do obsługi fontów TrueType w aplikacjach SDL3.
Pakiet zawiera przykładowy program "sdl2font", wyświetlający
przykładowy ciąg znaków zadanym fontem TrueType.

%description -l pt_BR.UTF-8
Esta é uma biblioteca que permite a utilização de fontes TrueType em
suas aplicações SDL3. Ela vem com o programa exemplo "sdl2font" que
mostra uma string exemplo para uma fonte TrueType fornecida.

%package devel
Summary:	Header files and more to develop SDL3_ttf applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL3_ttf
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL3_ttf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL3-devel >= 3.2.6
Requires:	freetype-devel >= 2.1.4
Requires:	plutosvg-devel

%description devel
Header files and more to develop SDL3_ttf applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL3_ttf.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL3_ttf.

%prep
%setup -q

%build
# Findplutosvg.cmake detects plutosvg include directory, but fails to include required plutovg one
export CFLAGS="%{rpmcflags} -I/usr/include/plutovg"
%cmake -B build \
	-DSDLTTF_INSTALL_MAN=ON \
	-DSDLTTF_STRICT=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install build/showfont $RPM_BUILD_ROOT%{_bindir}/sdl3-showfont

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/sdl3-showfont
%attr(755,root,root) %{_libdir}/libSDL3_ttf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL3_ttf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL3_ttf.so
%{_libdir}/cmake/SDL3_ttf
%{_includedir}/SDL3_ttf
%{_pkgconfigdir}/sdl3-ttf.pc
%{_mandir}/man3/SDL_TTF_*.3*
%{_mandir}/man3/TTF_*.3*
