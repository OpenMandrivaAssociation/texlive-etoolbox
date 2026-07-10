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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

