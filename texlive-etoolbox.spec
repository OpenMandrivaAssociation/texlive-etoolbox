Name:		texlive-etoolbox
Version:	56554
Release:	2
Summary:	Tool-box for LaTeX programmers using e-TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etoolbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The etoolbox package is a toolbox of programming facilities
geared primarily towards LaTeX class and package authors. It
provides LaTeX frontends to some of the new primitives provided
by e-TeX as well as some generic tools which are not strictly
related to e-TeX but match the profile of this package. Note
that the initial versions of this package were released under
the name elatex. The package provides functions that seem to
offer alternative ways of implementing some LaTeX kernel
commands; nevertheless, the package will not modify any part of
the LaTeX kernel.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etoolbox
%doc %{_texmfdistdir}/doc/latex/etoolbox

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
