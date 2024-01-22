Summary:	Simple DirectMedia Layer 2 - ttf handling
Summary(pl.UTF-8):	Biblioteka obsługi fontów TTF dla SDL2
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer 2 - Biblioteca de fontes TrueType
Name:		SDL2_ttf
Version:	2.22.0
Release:	1
License:	Zlib-like
Group:		Libraries
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL2_ttf-%{version}.tar.gz
# Source0-md5:	686e685caaa215d8fa1ac7bb02b2cf54
URL:		https://github.com/libsdl-org/SDL_ttf
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2.0.10
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.16
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	harfbuzz-devel >= 2.3.1
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	SDL2 >= 2.0.10
Requires:	freetype >= 2.1.4
Requires:	harfbuzz >= 2.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to use TrueType fonts in
your SDL2 applications. It comes with an example program "sdl2font"
which displays an example string for a given TrueType font file.

%description -l pl.UTF-8
Przykładowa biblioteka do obsługi fontów TrueType w aplikacjach SDL2.
Pakiet zawiera przykładowy program "sdl2font", wyświetlający
przykładowy ciąg znaków zadanym fontem TrueType.

%description -l pt_BR.UTF-8
Esta é uma biblioteca que permite a utilização de fontes TrueType em
suas aplicações SDL2. Ela vem com o programa exemplo "sdl2font" que
mostra uma string exemplo para uma fonte TrueType fornecida.

%package devel
Summary:	Header files and more to develop SDL2_ttf applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL2_ttf
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL2_ttf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel >= 2.0.8
Requires:	freetype-devel >= 2.1.4

%description devel
Header files and more to develop SDL2_ttf applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL2_ttf.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL2_ttf.

%package static
Summary:	Static SDL2_ttf library
Summary(pl.UTF-8):	Biblioteka statyczna SDL2_ttf
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento utilizando a SDL2_ttf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL2_ttf library.

%description static -l pl.UTF-8
Biblioteka statyczna SDL2_ttf.

%description static -l pt_BR.UTF-8
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
SDL2_ttf.

%prep
%setup -q

%{__rm} -r external/{freetype,harfbuzz}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-freetype-builtin \
	--disable-harfbuzz-builtin

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install .libs/showfont $RPM_BUILD_ROOT%{_bindir}/sdl2font

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%attr(755,root,root) %{_bindir}/sdl2font
%attr(755,root,root) %{_libdir}/libSDL2_ttf-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL2_ttf-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL2_ttf.so
%{_libdir}/cmake/SDL2_ttf
%{_includedir}/SDL2/SDL_ttf.h
%{_pkgconfigdir}/SDL2_ttf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2_ttf.a
