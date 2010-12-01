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

%global section free

%global jspspec 2.1
%global major_version 6
%global minor_version 0
%global micro_version 26
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

Name: tomcat6
Epoch: 0
Version: %{major_version}.%{minor_version}.%{micro_version}
Release: 14%{?dist}
Summary: Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group: Networking/Daemons
License: ASL 2.0
URL: http://tomcat.apache.org/
Source0: http://www.apache.org/dist/tomcat/tomcat-6/v%{version}/src/%{packdname}.tar.gz
Source1: %{name}-%{major_version}.%{minor_version}.conf
Source2: %{name}-%{major_version}.%{minor_version}.init
Source3: %{name}-%{major_version}.%{minor_version}.sysconfig
Source4: %{name}-%{major_version}.%{minor_version}.wrapper
Source5: %{name}-%{major_version}.%{minor_version}.logrotate
Source6: %{name}-%{major_version}.%{minor_version}-digest.script
Source7: %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8: servlet-api-OSGi-MANIFEST.MF
Source9: jsp-api-OSGi-MANIFEST.MF
Source10: %{name}-%{major_version}.%{minor_version}-log4j.properties
Patch0: %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1: %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2: %{name}-%{major_version}.%{minor_version}-CVE-2010-2227.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: jakarta-commons-collections
#BuildRequires: jakarta-commons-collections-tomcat5
BuildRequires: jakarta-commons-daemon
#BuildRequires: jakarta-commons-dbcp-tomcat5
#BuildRequires: jakarta-commons-pool-tomcat5
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: java-1.6.0-devel
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
Requires(pre): shadow-utils
Requires(pre): shadow-utils
Requires: jakarta-commons-daemon
Requires: jakarta-commons-logging
Requires: jakarta-commons-collections
Requires: java-1.6.0
Requires: procps
Requires: %{name}-lib = %{epoch}:%{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(post): /lib/lsb/init-functions
Requires(preun): /lib/lsb/init-functions
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

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
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.


%package log4j
Group: Internet/WWW/Dynamic Content
Summary: Log4j support for Apache Tomcat
Requires: jakarta-commons-logging

%description log4j
Log4j support for Apache Tomcat

%package lib
Group: Development/Compilers
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Internet/WWW/Dynamic Content
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet25
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Group: Development/Libraries/Java
Summary: Expression Language v1.0 API
Provides: el_1_0_api = %{epoch}:%{version}-%{release}
Provides: el_api = %{elspec}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

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
%setup -q -c -T -a 0
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) | xargs -t %{__rm}
pushd %{packdname}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar
popd

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-nodeps"
pushd %{packdname}
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with jakarta-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath jakarata-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
      -Dcommons-daemon.jsvc.tar.gz="HACK" \
      -Djasper-jdt.jar="$(build-classpath ecj)" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-dbcp.jar="$(build-classpath commons-dbcp)" \
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
   %{__rm} output/build/bin/HACK \
      output/build/bin/tomcat-native.tar.gz 
popd
pushd %{packdname}/output/dist/src/webapps/docs/appdev/sample/src
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
zip -u %{packdname}/output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{packdname}/output/build/lib/jsp-api.jar META-INF/MANIFEST.MF

%install
%{__rm} -rf $RPM_BUILD_ROOT
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
pushd %{packdname}/output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} %{SOURCE10} conf/log4j.properties
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
pushd %{packdname}/output/dist/webapps
    %{__cp} -a docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
popd
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
   %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api-%{version}.jar
   %{__mv} %{name}/servlet-api.jar \
      %{name}-servlet-%{servletspec}-api-%{version}.jar
   %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api-%{version}.jar
   %{__ln_s} %{name}-jsp-%{jspspec}-api-%{version}.jar \
      %{name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{name}-servlet-%{servletspec}-api-%{version}.jar \
      %{name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{name}-el-%{elspec}-api-%{version}.jar %{name}-el-%{elspec}-api.jar
popd

pushd %{packdname}/output/build
   %{_bindir}/build-jar-repository lib commons-collections \
    commons-dbcp commons-pool ecj 2>&1
# need to use -p here with b-j-r otherwise the examples webapp fails to
# load with a java.io.IOException
   %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
   # fix up jars to include version number
   for i in *.jar; do
      j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
      %{__mv} ${j}.jar ${j}-%{version}.jar
      %{__ln_s} ${j}-%{version}.jar ${j}.jar
    done
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api-%{version}.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api-%{version}.jar .
    %{__ln_s} ../%{name}-el-%{elspec}-api-%{version}.jar
    %{__cp} -p $(build-classpath commons-collections) .
    %{__cp} -p $(build-classpath log4j) .
    %{__ln_s} log4j log4j-%{version}.jar
#    %{__ln_s} $(build-classpath commons-dbcp) .
#    %{__ln_s} $(build-classpath commons-pool) .
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar
popd
pushd ${RPM_BUILD_ROOT}%{bindir}
   # fix up jars to include version number
   for i in *.jar; do
      j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
      %{__mv} ${j}.jar ${j}-%{version}.jar
      %{__ln_s} ${j}-%{version}.jar ${j}.jar
   done
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

# Link the juli jars into /usr/share/java/tomcat6
pushd ${RPM_BUILD_ROOT}%{libdir}
%{__ln_s} %{bindir}/tomcat-juli* .
popd

# Generate a depmap fragment javax.servlet:servlet-api pointing to 
# tomcat6-servlet-2.5-api for backwards compatibility
%add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{name}-servlet-api 

# Install the maven metadata
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd %{packdname}/output/dist/src/res/maven
for file in *.pom; do
   base=`basename $file .pom`
   # Some POMs don't actually have corresponding jar files in the current RPM
   if [ $base != 'dbcp' -a $base != 'juli-adapters' -a $base != 'juli-extras' ]; then
      sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $file
      %{__cp} -a $file ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-%{name}-$file
      # Some jar files have tomcat6 prepended and some don't, and some have their
      # canonical home outside of the tomcat6 subdirectory
      jppdir="JPP/%{name}"
      if [ $base = 'coyote' -o $base = 'jsp-api' -o $base = 'servlet-api' ]; then
         jpp="%{name}-$base"
         jppdir="JPP"
      else
         if [ $base = 'tribes' ]; then
            jpp=catalina-$base
         else
            if [ $base = 'juli' -o $base = 'coyote' ]; then
               jpp=tomcat-$base
            else
               jpp=$base
            fi
         fi
      fi

      if [ $base = 'jasper-jdt' ]; then
         %add_to_maven_depmap org.apache.tomcat $base %{version} JPP ecj 3.4.2
      else
         %add_to_maven_depmap org.apache.tomcat $base %{version} $jppdir $jpp %{version}
      fi
   fi
done


%clean
%{__rm} -rf $RPM_BUILD_ROOT


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

#%post lib
#%{_bindir}/build-jar-repository %{libdir} commons-collections-tomcat5 \
#    commons-dbcp-tomcat5 commons-pool-tomcat5 ecj 2>&1

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20500
%update_maven_depmap

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
   %{_javadir}/%{name}-el-%{elspec}-api.jar 20250

#%post webapps
# need to use -p here with b-j-r otherwise the examples webapp fails to
# load with a java.io.IOException
#%{_bindir}/build-jar-repository -p %{appdir}/examples/WEB-INF/lib \
#    taglibs-core.jar taglibs-standard.jar 2>&1

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

#%preun lib
#if [ "$1" = "0" ]; then
#    %{__rm} -f %{libdir}/\[commons-collections-tomcat5\].jar \
#        %{libdir}/\[commons-dbcp-tomcat5\].jar \
#        %{libdir}/\[commons-pool-tomcat5\].jar \
#        %{libdir}/\[ecj\].jar >/dev/null 2>&1
#fi

%postun
%update_maven_depmap
#%{__rm} -rf %{appdir}
#%{__rm} -rf %{confdir}
#%{__rm} -rf %{libdir}

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
%defattr(0644,root,tomcat,0775)
%doc %{packdname}/{LICENSE,NOTICE,RELEASE*}
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
#%dir %{confdir}
#%dir %{confdir}/Catalina
%attr(0765,root,tomcat) %dir %{confdir}/Catalina/localhost
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%attr(0664,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/web.xml
%attr(0765,tomcat,root) %dir %{cachedir}
%attr(0765,tomcat,root) %dir %{tempdir}
%attr(0765,tomcat,root) %dir %{workdir}
%attr(0765,root,tomcat) %dir %{logdir}
%dir %{homedir}
#%attr(0765,root,tomcat) %{homedir}/conf
%{bindir}/bootstrap-%{version}.jar
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{bindir}/tomcat-juli-%{version}.jar
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
%defattr(0644,root,root,0775)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%defattr(0644,root,root,0755)
%{appdir}/docs

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-jsp-%{jspspec}*.jar
%{_mavenpomdir}/JPP-%{name}-jsp-api.pom

%files log4j
%defattr(0644,root,tomcat,0775)
%config(noreplace) %{confdir}/log4j.properties
%{libdir}/log4j.jar
%{libdir}/log4j-%{version}.jar

%files lib
%defattr(0644,root,root,0755)
%{libdir}

%files servlet-%{servletspec}-api
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-servlet-%{servletspec}*.jar
%{_mavendepmapfragdir}/%{name}-servlet-api
%{_mavenpomdir}/JPP-%{name}-servlet-api.pom

%files el-%{elspec}-api
%defattr(0665,root,root,0755)
%{_javadir}/%{name}-el-%{elspec}-api-%{version}.jar
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}/%{name}-el-%{elspec}-api-%{version}.jar
%{_mavenpomdir}/JPP-%{name}-el-api.pom

%files webapps
%defattr(0644,root,tomcat,0775)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

%changelog
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
