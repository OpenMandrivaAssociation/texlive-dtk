%global tl_name dtk
%global tl_revision 71776

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.10f
Release:	%{tl_revision}.1
Summary:	Document class for the journal of DANTE
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/usergrps/dante/dtk
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a class and style file for typesetting "Die
TeXnische Komodie" -- the communications of the German TeX Users Group
DANTE e.V. The arrangement means that the class may be used by article
writers to typeset a single article, as well as to produce the complete
journal.

