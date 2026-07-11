%global tl_name marginalia
%global tl_revision 79621

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.83.23
Release:	%{tl_revision}.1
Summary:	Marginal content anywhere with automatic adjustment for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/marginalia
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginalia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginalia.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginalia.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LuaLaTeX package allows the placement of marginal content (such as
notes) anywhere, without \marginpar's limits, and automatically adjusts
positions to prevent overlaps or content being pushed off the page, and
offers key-value settings that allow fine-grained customization.

