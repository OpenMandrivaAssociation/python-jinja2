%define tarname Jinja2
%define fname   jinja2
%define name	python-jinja2
%define version 2.6
%define release 3

# jinja requires itself ( as python-sphinx use it ) to build doc
%define enable_doc 0

Summary:	Python template engine
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-jinja
Requires:	python >= 2.4
Suggests:	python-markupsafe
BuildRequires:	python-devel >= 2.4, python-setuptools
%if %enable_doc
BuildRequires:	python-sphinx
%endif

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%setup -q -n %{tarname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build 
%if %enable_doc
%make -C docs html
%endif

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__rm -rf docs/_build/html/.buildinfo

%check
make test

%files
%defattr(-,root,root)
%{py_puresitedir}/%{fname}
%{py_puresitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info
%doc AUTHORS CHANGES LICENSE examples 
%if %enable_doc
%doc docs/_build/html
%endif


%changelog
* Mon Jul 25 2011 Lev Givon <lev@mandriva.org> 2.6-1
+ Revision: 691490
- Update to 2.6.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.5-5
+ Revision: 667940
- mass rebuild

* Wed Jan 26 2011 Lev Givon <lev@mandriva.org> 2.5.5-4
+ Revision: 632764
- Rebuild to provide pythonegg(Jinja2).

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 2.5.5-3mdv2011.0
+ Revision: 590403
- reenable doc now python-kinja have compiled for 2.7

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 2.5.5-2mdv2011.0
+ Revision: 590400
- disable doc ( as jinja2 requires itself for that )
- rebuild for python 2.7

* Mon Oct 18 2010 Lev Givon <lev@mandriva.org> 2.5.5-1mdv2011.0
+ Revision: 586681
- Update to 2.5.5.

* Sun Oct 17 2010 Lev Givon <lev@mandriva.org> 2.5.4-1mdv2011.0
+ Revision: 586393
- Update to 2.5.4.

* Wed Aug 18 2010 Lev Givon <lev@mandriva.org> 2.5.2-1mdv2011.0
+ Revision: 571216
- Update to 2.5.2.

* Tue Aug 17 2010 Lev Givon <lev@mandriva.org> 2.5.1-1mdv2011.0
+ Revision: 571048
- Update to 2.5.1.
  Change to noarch because speedups are now in markupsafe package.

* Sun May 30 2010 Lev Givon <lev@mandriva.org> 2.5-1mdv2011.0
+ Revision: 546592
- Update to 2.5.

* Tue Apr 20 2010 Lev Givon <lev@mandriva.org> 2.4.1-1mdv2010.1
+ Revision: 537097
- Update to 2.4.1.

* Mon Mar 15 2010 Lev Givon <lev@mandriva.org> 2.3.1-2mdv2010.1
+ Revision: 519116
- Obsolete python-jinja.

* Fri Feb 19 2010 Frederik Himpe <fhimpe@mandriva.org> 2.3.1-1mdv2010.1
+ Revision: 508510
- Update to new version 2.3.1

* Wed Feb 10 2010 Lev Givon <lev@mandriva.org> 2.3-1mdv2010.1
+ Revision: 503884
- Update to 2.3.

* Thu Nov 12 2009 Lev Givon <lev@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 465419
- Update to 2.2.1.

* Fri May 22 2009 Lev Givon <lev@mandriva.org> 2.1.1-1mdv2010.0
+ Revision: 378570
- imported package python-jinja2


