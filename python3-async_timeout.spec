#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Timeout context manager for asyncio programs
Summary(pl.UTF-8):	Zarządca kontekstu z limitem czasu dla programów asyncio
Name:		python3-async_timeout
Version:	4.0.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/async-timeout/
Source0:	https://files.pythonhosted.org/packages/source/a/async-timeout/async-timeout-%{version}.tar.gz
# Source0-md5:	10571272b2e0fab839ec23f8293bf482
URL:		https://pypi.org/project/async-timeout/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:45
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-asyncio
BuildRequires:	python3-pytest-cov
%if "%{py3_ver}" < "3.8"
BuildRequires:	python3-typing_extensions >= 3.6.5
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asyncio-compatible timeout context manager.

%description -l pl.UTF-8
Zarządca kontekstów z limitem czasu, zgodny z asyncio.

%prep
%setup -q -n async-timeout-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_asyncio.plugin,pytest_cov.plugin" \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/async_timeout
%{py3_sitescriptdir}/async_timeout-%{version}-py*.egg-info
