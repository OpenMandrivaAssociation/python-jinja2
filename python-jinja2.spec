%define tarname Jinja2
%define fname jinja2

# jinja requires itself ( as python-sphinx use it ) to build doc
%bcond_with doc

Summary:	Python template engine
Name:		python-jinja2
Version:	3.1.6
Release:	3
License:	BSD
Group:		Development/Python
Url:		https://jinja.palletsprojects.com/
Source0:	https://github.com/pallets/jinja/archive/%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	make
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(markupsafe)
%if %{with doc}
BuildRequires:	python%{pyver}dist(sphinx)
%endif
Requires:	python >= 3.0
Suggests:	python-markupsafe
%rename python-jinja
%rename python3-jinja2

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%build -a
%if %{with doc}
%make_build -C docs html
%endif

%files
%doc examples
%dir %{py_puresitedir}/%{fname}
%{py_puresitedir}/%{fname}/*
%{py_puresitedir}/%{fname}-%{version}.dist-info
%if %{with doc}
%doc docs/_build/html
%endif
