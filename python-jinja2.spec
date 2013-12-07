%define tarname Jinja2
%define fname   jinja2

# jinja requires itself ( as python-sphinx use it ) to build doc
%define enable_doc 1

Summary:	Python template engine
Name:		python-jinja2
Version:	2.7.1
Release:	5
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
Source0:	https://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel >= 2.4, python-setuptools, python3-devel, python3-distribute
BuildRequires:	python-markupsafe
BuildRequires:	python3-markupsafe
%if %enable_doc
BuildRequires:	python-sphinx
%endif
Requires:	python >= 2.4
Obsoletes:	python-jinja
Suggests:	python-markupsafe

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%package -n python3-jinja2
Summary:	Python template engine
Group:		Development/Python
Requires:	python3
 
%description -n python3-jinja2
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%setup -q -c

mv %{tarname}-%{version} python2
cp -r python2 python3

%build
pushd python2
PYTHONDONTWRITEBYTECODE=  python setup.py build
%if %enable_doc
%make -C docs html
%endif
popd

pushd python3
PYTHONDONTWRITEBYTECODE=  python3 setup.py build
%if %enable_doc
%make -C docs html
%endif
popd

%check
pushd python2
make test 
popd

pushd python3
make test 
popd

%install
pushd python2
%{__python} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-jinja2 
%doc python2/AUTHORS python2/CHANGES python2/LICENSE python2/examples
%{py_puresitedir}/%{fname}/*
%{py_puresitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info
%if %enable_doc
%doc python2/docs/_build/html
%endif

%files -n python3-jinja2
%doc python3/AUTHORS python3/CHANGES python3/LICENSE python3/examples
%{py3_puresitedir}/%{fname}/*
%{py3_puresitedir}/%{tarname}-%{version}-py%{py3_ver}.egg-info
%if %enable_doc
%doc python3/docs/_build/html
%endif

