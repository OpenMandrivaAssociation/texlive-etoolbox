# revision 20922
# category Package
# catalog-ctan /macros/latex/contrib/etoolbox
# catalog-date 2011-01-03 19:54:22 +0100
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-etoolbox
Version:	2.1
Release:	5
Summary:	Tool-box for LaTeX programmers using e-TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etoolbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/etoolbox/etoolbox.def
%{_texmfdistdir}/tex/latex/etoolbox/etoolbox.sty
%doc %{_texmfdistdir}/doc/latex/etoolbox/README
%doc %{_texmfdistdir}/doc/latex/etoolbox/etoolbox.pdf
%doc %{_texmfdistdir}/doc/latex/etoolbox/etoolbox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 751642
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 718380
- texlive-etoolbox
- texlive-etoolbox
- texlive-etoolbox
- texlive-etoolbox

