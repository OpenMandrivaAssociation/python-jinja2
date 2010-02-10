%define tarname Jinja2
%define name	python-jinja2
%define version 2.3
%define release %mkrel 1

Summary:	Python template engine
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
Source1:	html.tar.bz2
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.4
BuildRequires:	python-devel >= 2.4, python-setuptools

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%setup -q -n %{tarname}-%{version}
tar pjxf %SOURCE1 

%build
%__python setup.py --with-speedups build 

%install
%__rm -rf %{buildroot}
%__python setup.py --with-speedups install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc AUTHORS CHANGES LICENSE examples html
