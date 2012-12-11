%define	pkgname fenv
%define name	octave-%{pkgname}
%define version 0.1.0

Summary:	Change floating point precision in Octave
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/fenv/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0
BuildRequires:  octave-devel >= 3.0.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel

%description
On supported architectures, change the rounding mode of the floating
point arithmetics (to nearest, up, down, to zero) or change the
precision of the arithmetical operations (single, double, double
extended) in Octave. Experimentally test the properties of the
floating point arithmetics.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}



%changelog
* Sun Aug 21 2011 Lev Givon <lev@mandriva.org> 0.1.0-1mdv2012.0
+ Revision: 696032
- import octave-fenv


