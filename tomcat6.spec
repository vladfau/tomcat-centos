# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global jspspec 2.1
%global major_version 6
%global minor_version 0
%global micro_version 30
%global packdname apache-tomcat-%{version}-src
%global servletspec 2.5
%global elspec 2.1
%global tcuid 91

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global bindir %{_datadir}/%{name}/bin
%global confdir %{_sysconfdir}/%{name}
%global homedir %{_datadir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %{_sysconfdir}/init.d

Name:          tomcat6
Epoch:         0
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       1%{?dist}
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group:         Networking/Daemons
License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-6/v%{version}/src/%{packdname}.tar.gz
Source1:       %{name}-%{major_version}.%{minor_version}.conf
Source2:       %{name}-%{major_version}.%{minor_version}.init
Source3:       %{name}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{name}-%{major_version}.%{minor_version}.wrapper
Source5:       %{name}-%{major_version}.%{minor_version}.logrotate
Source6:       %{name}-%{major_version}.%{minor_version}-digest.script
Source7:       %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source10:      %{name}-%{major_version}.%{minor_version}-log4j.properties
Patch0:        %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2:        %{name}-%{major_version}.%{minor_version}-rhbz-674601.patch
BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: jakarta-commons-collections
BuildRequires: apache-commons-daemon
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: java-1.6.0-devel
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
Requires:      apache-commons-daemon
Requires:      apache-commons-logging
Requires:      apache-commons-collections
Requires:      java-1.6.0
Requires:      procps
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}
Requires(pre):    shadow-utils
Requires(pre):    shadow-utils
Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(post):   redhat-lsb
Requires(preun):  redhat-lsb
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# added after log4j sub-package was removed
Provides:         %{name}-log4j = %{epoch}:%{version}-%{release}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: System Environment/Applications
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: System Environment/Applications
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Documentation
Summary: Javadoc generated documentation for Apache Tomcat

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Group: Internet/WWW/Dynamic Content
Summary: Apache Tomcat JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp21
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): chkconfig
Requires(postun): chkconfig

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.


%package lib
Group: Development/Compilers
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj
Requires: apache-commons-collections
Requires: apache-commons-dbcp
Requires: apache-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Internet/WWW/Dynamic Content
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet25
Requires(post): chkconfig
Requires(postun): chkconfig

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Group: Development/Libraries/Java
Summary: Expression Language v1.0 API
Provides: el_1_0_api = %{epoch}:%{version}-%{release}
Provides: el_api = %{elspec}
Requires(post): chkconfig
Requires(postun): chkconfig

%description el-%{elspec}-api
Expression Language 1.0.

%package webapps
Group: System Environment/Applications
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0
%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar

%build
export OPT_JAR_LIST="xalan-j2-serializer"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath apache-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath apache-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Djasper-jdt.jar="$(build-classpath ecj)" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-dbcp.jar="$(build-classpath apache-commons-dbcp)" \
      -Dtomcat-native.tar.gz="HACK" \
      -Dversion="%{version}" \
      -Dversion.build="%{micro_version}"
   # javadoc generation
   %{ant} -f dist.xml dist-prepare
   %{ant} -f dist.xml dist-source
   %{ant} -f dist.xml dist-javadoc
    # remove some jars that we'll replace with symlinks later
   %{__rm} output/build/bin/commons-daemon.jar \
           output/build/lib/ecj.jar
    # remove the cruft we created
   %{__rm} output/build/bin/tomcat-native.tar.gz
pushd output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jsp-api.jar META-INF/MANIFEST.MF

%install
# build initial path structure
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} %{SOURCE10} conf/log4j.properties
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
%{__cp} -a output/dist/webapps/docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}

%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__install} -m 0644 %{SOURCE2} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
%{__install} -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{name}
%{__ln_s} %{name} ${RPM_BUILD_ROOT}%{_sbindir}/d%{name}
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-tool-wrapper
# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
   %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   %{__mv} %{name}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api.jar
   %{__ln_s} %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository lib apache-commons-collections \
                                        apache-commons-dbcp apache-commons-pool ecj 2>&1
    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../%{name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath apache-commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath apache-commons-dbcp) commons-dbcp.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar

    # Link the juli jar into /usr/share/java/tomcat6
    %{__ln_s} %{bindir}/tomcat-juli.jar .
popd

# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# install sample webapp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{appdir}/sample
pushd ${RPM_BUILD_ROOT}%{appdir}/sample
%{jar} xf ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
popd
%{__rm} ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war


# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat6-servlet-2.5-api for backwards compatibility
%add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here)
%add_to_maven_depmap org.mortbay.jetty servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{name}-servlet-api

# Install the maven metadata
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

# we won't install dbcp, juli-adapters and juli-extras pom files
for pom in annotations-api.pom catalina.pom jasper-el.pom jasper.pom \
           catalina-ha.pom el-api.pom; do
    %{__cp} -a $pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP/%{name} $base
done

# servlet-api jsp-api and el-api are not in tomcat6 subdir, since they are widely re-used elsewhere
for pom in jsp-api.pom servlet-api.pom el-api.pom;do
    %{__cp} -a $pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-%{name}-$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP %{name}-$base
done

# two special pom where jar files have different names
%{__cp} -a tribes.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-catalina-tribes.pom
%add_to_maven_depmap org.apache.tomcat tribes %{version} JPP/%{name} catalina-tribes

%{__cp} -a juli.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-tomcat-juli.pom
%add_to_maven_depmap org.apache.tomcat juli %{version} JPP/%{name} tomcat-juli


%pre
# add the tomcat user and group
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /bin/sh -r -d %{homedir} tomcat 2>/dev/null || :
# Save the conf, app, and lib dirs
# due to rbgz 640686. Copy them to the _tmppath so we don't pollute
# the tomcat file structure
[ -d %{appdir} ] && %{__cp} -rp %{appdir} %{_tmppath}/%{name}-webapps.bak || :
[ -d %{confdir} ] && %{__cp} -rp %{confdir} %{_tmppath}/%{name}-confdir.bak || :
[ -d %{libdir}  ] && %{__cp} -rp %{libdir} %{_tmppath}/%{name}-libdir.bak || :

%post
# install but don't activate
/sbin/chkconfig --add %{name}
%update_maven_depmap

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20100

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20500
%update_maven_depmap

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
   %{_javadir}/%{name}-el-%{elspec}-api.jar 20250


# move the temporary backups to the correct tomcat directory
# due to rhbz 640686
%posttrans
if [ -d %{_tmppath}/%{name}-webapps.bak ]; then
  %{__cp} -rp %{_tmppath}/%{name}-webapps.bak/* %{appdir}
  %{__rm} -rf %{_tmppath}/%{name}-webapps.bak
fi
if [ -d %{_tmppath}/%{name}-libdir.bak ]; then
  %{__cp} -rp %{_tmppath}/%{name}-libdir.bak/* %{libdir}
  %{__rm} -rf %{_tmppath}/%{name}-libdir.bak
fi
if [ -d %{_tmppath}/%{name}-confdir.bak ]; then
  %{__cp} -rp %{_tmppath}/%{name}-confdir.bak/* %{confdir}
  %{__rm} -rf %{_tmppath}/%{name}-confdir.bak
fi

%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir} %{tempdir}
if [ "$1" = "0" ]; then
    %{_initrddir}/%{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi


%postun
%update_maven_depmap

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
    %update_maven_depmap
fi

%postun el-%{elspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove elspec \
        %{_javadir}/%{name}-el-%{elspec}-api.jar
fi

%files
%defattr(-,root,tomcat,-)
%doc {LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/%{name}-digest
%attr(0755,root,root) %{_bindir}/%{name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0765,root,tomcat) %dir %{basedir}
%attr(0765,root,tomcat) %dir %{appdir}
%attr(0765,root,tomcat) %dir %{confdir}
%attr(0765,root,tomcat) %dir %{confdir}/Catalina
%attr(0765,root,tomcat) %dir %{confdir}/Catalina/localhost
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%config(noreplace) %{confdir}/log4j.properties
%attr(0664,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/web.xml
%attr(0765,tomcat,root) %dir %{cachedir}
%attr(0765,tomcat,root) %dir %{tempdir}
%attr(0765,tomcat,root) %dir %{workdir}
%attr(0765,root,tomcat) %dir %{logdir}
%dir %{homedir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{bindir}/tomcat-juli.jar
%{homedir}/lib
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/conf
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*.pom
# Exclude the POMs that are in sub-packages
%exclude %{_mavenpomdir}/*api*

%files admin-webapps
%defattr(-,root,root,-)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%defattr(-,root,root,-)
%{appdir}/docs

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%defattr(-,root,root,-)
%{_javadir}/%{name}-jsp-%{jspspec}*.jar
%{_javadir}/%{name}-jsp-api.jar
%{_mavenpomdir}/JPP-%{name}-jsp-api.pom

%files lib
%defattr(-,root,root,-)
%{libdir}

%files servlet-%{servletspec}-api
%defattr(-,root,root,-)
%{_javadir}/%{name}-servlet-%{servletspec}*.jar
%{_javadir}/%{name}-servlet-api.jar
%{_mavendepmapfragdir}/%{name}-servlet-api
%{_mavenpomdir}/JPP-%{name}-servlet-api.pom

%files el-%{elspec}-api
%defattr(-,root,root,-)
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}-el-api.jar
%{_javadir}/%{name}/%{name}-el-%{elspec}-api.jar
%{_mavenpomdir}/JPP-%{name}-el-api.pom

%files webapps
%defattr(-,root,tomcat,-)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

%changelog
* Thu Feb 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.30-1
- Update to 6.0.30.
- Drop jdt-core.pom which is gone upstream now.

* Wed Feb 2 2011 David Knox <dknox@redhat.com> 0:6.0.29-3
- Resolves rhbz# 674601 - JDK Double.parseDouble DoS

* Mon Jan 17 2011 David Knox <dknox@redhat.com> 0:6.0.29-2
- Resolves: rhbz# 669969 - tomcat-jdbc missing
- Resolves problem with multiple instances of tomcat services. References to 
- hardcoded directory locations have been changed to ${CATALINA_HOME]
- to avoid confusion

* Mon Jan 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.29-1
- Update to new upstream.
- Simplify buildroot.
- Don't require files but packages.

* Wed Dec  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:6.0.26-18
- Add api jars without spec version symlinks
- Remove clean section
- Remove whitespaces at the EOLs

* Mon Dec  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:6.0.26-17
- Add jetty to servlet-api depmap

* Thu Dec  2 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:6.0.26-16
- Fixes according to guidelines (versionless jars, no random defattrs)
- Simplify pom installation by splitting to more steps
- Formatting cleanups
- Removed log4j subpackage (used bundled log4j, replaced by symlink)

* Thu Dec  2 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:6.0.26-15
- Fix log4j symlink (Resolves rhbz#654660)

* Mon Nov 29 2010 David Knox <dknox@redhat.com> 0:6.0.26-14
- Resolving rhbz 640686: save appdir, confdir, and libdir during
- pre and copy them back during posttrans. The directories are
- copied to /var/tmp. They are copied back during posttrans and
- removed from /var/tmp.

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 0:6.0.26-13
- Added javax.servlet:servlet-api depmap entry to servlet-2.5-api subpackage

* Thu Oct 14 2010 David Knox <dknox@redhat.com> 0:6.0.26-12
- Resolves rhbz#640686 - Upgrade of tomcat6 wipes out directories
- WARNING - Back up all files that need to be preserved before
- package update or uninstall - WARNING
- Resolves: rhbz#638914 - update versions of commons-collections,
- commons-dbcp, and commons-pool

* Thu Oct 07 2010 David Knox <dknox@redhat.com> 0:6.0.26-11
- resolves rhbz#640837 - tomcat user requires login shell

* Mon Oct 04 2010 David Knox <dknox@redhat.com> 0:6.0.26-10
- ant-nodeps is breaking the build. Put ant-nodeps on the
- OPT_JAR_LIST

* Fri Oct 01 2010 David Knox <dknox@rehat.com> 0:6.0.26-9
- Resolves rhbz#575341 - Additionally created instances of Tomcat
- are broken

* Fri Jul 02 2010 David Knox <dknox@rehat.com> 0:6.0.26-8
- LSB initscript compliance

* Thu Jul 01 2010 David Knox <dknox@redhat.com> 0:6.0.26-7
- Made elspec the standard for elspec %post and %postun.

* Tue Jun 29 2010 David Knox <dknox@redhat.com> 0:6.0.26-6
- Completed package and file sections. Added el-spec. Fixed
- directory permission problems.

* Thu May 6 2010 David Knox <dknox@redhat.com> 0:6.0.26-5
- Working on 589145. Tomcat can't find java compiler for java.

* Tue Apr 08 2010 David Knox <dknox@redhat.com> 0:6.0.26-4
- Moved build-jar-repository to later in the install process.

* Tue Apr 06 2010 David Knox <dknox@redhat.com> 0:6.0.26-3
- Incremented the Release tag to 3 to avoid any confusion about which
- is the most recent

* Tue Apr 06 2010 David Knox <dknox@redhat.com> 0:6.0.26-1
- Solved packaging problems involving taglibs-standard
- Solved packaging problems involving jakarta-commons
- Corrected Requires(post) to Requires and checked companion BuildRequires

* Mon Mar 29 2010 David Knox <dknox@redhat.com> 0:6.0.26-2
- Update source to tomcat6.0.26
- Bugzilla 572357 - Please retest.
- OSGi manifests for servlet-api and jsp-api


* Fri Mar 26 2010 Mary Ellen Foster <mefoster@gmail.com> 0:6.0.24-2
- Add maven POMs and metadata
- Link tomcat6-juli into /usr/share/java/tomcat6

* Mon Mar 1 2010 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.24-1
- Update to 6.0.24.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.20-2
- Drop file requires on /usr/share/java/ecj.jar.

* Mon Nov 9 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.20-1
- Update to 6.0.20. Fixes CVE-2009-0033,CVE-2009-0580.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:6.0.18-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 1 2009 Alexander Kurtakov <akurtako@redhat.com> 0:6.0.18-9.2
- Add OSGi manifest for servlet-api.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:6.0.18-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 02 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-8.1
- build for Fedora

* Tue Dec 02 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-8
- fix directory ownership

* Thu Nov 13 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-7
- add Requires for update-alternatives

* Tue Oct 07 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-6
- use lsb_release instead of lsb-release to get the distributor

* Tue Oct 07 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-5
- fix initscript messages on Mandriva Linux
- fix help message in initscript

* Wed Oct 01 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-4
- redefine %%_initrddir for FHS-compliance
- make initscript LSB-complaint

* Fri Sep 26 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-3
- fix status in initscript

* Thu Sep 25 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-2
- remove initscripts and /sbin/service requirement
- call initscript directly without using /sbin/service
- require /sbin/chkconfig instead of chkconfig
- remove chkconfig requirement from packages that don't require it

* Tue Aug 26 2008 David Walluck <dwalluck@redhat.com> 0:6.0.18-1
- 6.0.18
- Resolves: CVE-2008-1232, CVE-2008-1947, CVE-2008-2370, CVE-2008-2938
- fix definition of java.security.policy with d%%{name} start-security
- don't pass $CATALINA_OPTS with d%%{name} stop
- redefine tempdir and workdir for tmpwatch workaround
- change eclipse-ecj references to ecj

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:6.0.16-1.8
- drop repotag

* Fri Apr 04 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.7.fc9
- version jsp and servlet Provides with their spec versions
- remove Obsoletes/Provides for servletapi6 package as it can co-exist
- check for java-functions existence in wrapper script
- move d%%{name} to %%{name} and create symlink for d%%{name}
- improve status function in initscript
- change license to ASL 2.0 again as per Fedora guidelines

* Mon Mar 24 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.6.fc9
- remove Requires: tomcat-native
- put back original JPackage Group (except javadoc) and License tags
- add Provides for jsp and servlet
- use ant macro
- build and install sample webapp
- call /sbin/service to stop service on uninstall
- remove references to $RPM_BUILD_DIR
- use copy instead of move to fix short-circuit install build
- remove prebuilt sample.war
- remove Thumbs.db files
- add Requires: java >= 0:1.6.0

* Wed Mar 19 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.5.fc9
- explicitly unset CLASSPATH
- explicitly set OPT_JAR_LIST to include ant/ant-trax

* Tue Mar 18 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.4.fc9
- remove BuildRequires: sed
- remove specific references to icedtea

* Mon Mar 17 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.3.fc9
- add digest and tool-wrapper scripts
- Requires: tomcat-native

* Fri Mar 7 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.2.fc9
- use %%{_var} for appdir instead of /srv
- use ${JAVACMD} for java executable in wrapper script
- use built-in status function in initscript where possible
- add missing require on procps for status function
- fix java.library.path setting in %%{_sysconfdir}/sysconfig/%%{name}
- add patch to document webapps in %%{_sysconfdir}/%%{name}/tomcat-users.xml
- remove %%{appdir}/ROOT/admin
- move %%{_bindir}/d%%{name} to %%{_sbindir}/d%%{name}

* Mon Mar 3 2008 David Walluck <dwalluck@redhat.com> 0:6.0.16-1jpp.1.fc9
- use %%{_initrddir} macro instead of %%{_sysconfdir}/init.d (rhbz #153187)
- fix java.library.path setting in %%{name}.conf (rhbz #253605)
- fix incorrect initscript output (rhbz #380921)
- update initscript (rhbz #247077)
- add logrotate support
- fix strange-permission
- fix %%prep
- replace /var with %%{_var}
- replace %%{_localstatedir} with %%{_var}
- use %%{logdir} where possible
- call build-jar-repository with full path in scriptlets
- remove file-based requires
- build with icedtea and set as the default JAVA_HOME in %%{name}.conf
- fix non-standard-group
- change ecj references to eclipse-ecj
- change Apache Software License 2.0 to ASL 2.0 for rpmlint

* Fri Feb  8 2008 Jason Corley <jason.corley@gmail.com> - 0:6.0.16-1jpp
- update to 6.0.16

* Sun Dec  2 2007 Jason Corley <jason.corley@gmail.com> - 0:6.0.14-2jpp
- add /etc/tomcat6/Catalina/localhost (Alexander Kurtakov)

* Tue Aug 14 2007 Jason Corley <jason.corley@gmail.com> 0:6.0.14-1jpp
- first JPackage release
