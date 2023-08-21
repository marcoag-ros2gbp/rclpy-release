%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rclpy
Version:        5.0.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rclpy package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-action-msgs
Requires:       ros-rolling-ament-index-python
Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-lifecycle-msgs
Requires:       ros-rolling-rcl
Requires:       ros-rolling-rcl-action
Requires:       ros-rolling-rcl-interfaces
Requires:       ros-rolling-rcl-lifecycle
Requires:       ros-rolling-rcl-logging-interface
Requires:       ros-rolling-rcl-yaml-param-parser
Requires:       ros-rolling-rmw
Requires:       ros-rolling-rmw-implementation
Requires:       ros-rolling-rosgraph-msgs
Requires:       ros-rolling-rosidl-runtime-c
Requires:       ros-rolling-rpyutils
Requires:       ros-rolling-unique-identifier-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-lifecycle-msgs
BuildRequires:  ros-rolling-pybind11-vendor
BuildRequires:  ros-rolling-python-cmake-module
BuildRequires:  ros-rolling-rcl
BuildRequires:  ros-rolling-rcl-action
BuildRequires:  ros-rolling-rcl-interfaces
BuildRequires:  ros-rolling-rcl-lifecycle
BuildRequires:  ros-rolling-rcl-logging-interface
BuildRequires:  ros-rolling-rcl-yaml-param-parser
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-rcutils
BuildRequires:  ros-rolling-rmw
BuildRequires:  ros-rolling-rmw-implementation
BuildRequires:  ros-rolling-rmw-implementation-cmake
BuildRequires:  ros-rolling-rosidl-runtime-c
BuildRequires:  ros-rolling-unique-identifier-msgs
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cmake-pytest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-rosidl-generator-py
BuildRequires:  ros-rolling-test-msgs
%endif

%description
Package containing the Python client.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Aug 21 2023 Shane Loretz <sloretz@openrobotics.org> - 5.0.1-1
- Autogenerated by Bloom

* Tue Jul 11 2023 Shane Loretz <sloretz@openrobotics.org> - 5.0.0-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Shane Loretz <sloretz@openrobotics.org> - 4.2.2-1
- Autogenerated by Bloom

* Thu May 11 2023 Shane Loretz <sloretz@openrobotics.org> - 4.2.1-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Shane Loretz <sloretz@openrobotics.org> - 4.2.0-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Shane Loretz <sloretz@openrobotics.org> - 4.1.0-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Shane Loretz <sloretz@openrobotics.org> - 4.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Shane Loretz <sloretz@openrobotics.org> - 3.10.0-2
- Autogenerated by Bloom
