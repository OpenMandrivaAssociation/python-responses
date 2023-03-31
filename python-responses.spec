Name:		python-responses
Version:	0.22.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/responses/responses-%{version}.tar.gz
Summary:	A utility library for mocking out the `requests` Python library.
URL:		https://pypi.org/project/responses/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
A utility library for mocking out the `requests` Python library.

%prep
%autosetup -p1 -n responses-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{py_puresitedir}/responses
%{py_puresitedir}/responses*.egg-info
