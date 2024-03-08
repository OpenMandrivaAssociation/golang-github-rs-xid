# Run tests in check section
%bcond_without check

# https://github.com/rs/xid
%global goipath		github.com/rs/xid
%global forgeurl	https://github.com/rs/xid
Version:		1.5.0

%gometa

Summary:	A globally unique id generator thought for the web
Name:		golang-github-rs-xid

Release:	1
Source0:	https://github.com/rs/xid/archive/v%{version}/xid-%{version}.tar.gz
URL:		https://github.com/rs/xid
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Package xid is a globally unique id generator library,
ready to safely be used directly in your server code.

Xid uses the Mongo Object ID algorithm to generate
globally unique ids with a different serialization
(base32hex) to make it shorter when transported as
a string.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n xid-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

