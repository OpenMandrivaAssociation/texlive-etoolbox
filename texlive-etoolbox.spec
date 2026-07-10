%global tl_name etoolbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5m
Release:	%{tl_revision}.1
Summary:	e-TeX tools for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etoolbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etoolbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a toolbox of programming facilities geared primarily
towards LaTeX class and package authors. It provides LaTeX frontends to
some of the new primitives provided by e-TeX as well as some generic
tools which are not strictly related to e-TeX but match the profile of
this package. Note that the initial versions of this package were
released under the name elatex. The package provides functions that seem
to offer alternative ways of implementing some LaTeX kernel commands;
nevertheless, the package will not modify any part of the LaTeX kernel.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/etoolbox
%dir %{_datadir}/texmf-dist/tex/latex/etoolbox
%doc %{_datadir}/texmf-dist/doc/latex/etoolbox/README.md
%doc %{_datadir}/texmf-dist/doc/latex/etoolbox/etoolbox.pdf
%doc %{_datadir}/texmf-dist/doc/latex/etoolbox/etoolbox.tex
%{_datadir}/texmf-dist/tex/latex/etoolbox/etoolbox.def
%{_datadir}/texmf-dist/tex/latex/etoolbox/etoolbox.sty
