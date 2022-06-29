#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-warp
Version  : 0.2.0
Release  : 16
URL      : https://cran.r-project.org/src/contrib/warp_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/warp_0.2.0.tar.gz
Summary  : Group Dates
Group    : Development/Tools
License  : MIT
Requires: R-warp-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
# warp
<!-- badges: start -->
[![Travis build
status](https://travis-ci.org/DavisVaughan/warp.svg?branch=master)](https://travis-ci.org/DavisVaughan/warp)
[![Codecov test
coverage](https://codecov.io/gh/DavisVaughan/warp/branch/master/graph/badge.svg)](https://codecov.io/gh/DavisVaughan/warp?branch=master)
[![R build
status](https://github.com/DavisVaughan/warp/workflows/R-CMD-check/badge.svg)](https://github.com/DavisVaughan/warp)
<!-- badges: end -->

%package lib
Summary: lib components for the R-warp package.
Group: Libraries

%description lib
lib components for the R-warp package.


%prep
%setup -q -c -n warp
cd %{_builddir}/warp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641147811

%install
export SOURCE_DATE_EPOCH=1641147811
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library warp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library warp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library warp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc warp || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/warp/DESCRIPTION
/usr/lib64/R/library/warp/INDEX
/usr/lib64/R/library/warp/LICENSE
/usr/lib64/R/library/warp/Meta/Rd.rds
/usr/lib64/R/library/warp/Meta/features.rds
/usr/lib64/R/library/warp/Meta/hsearch.rds
/usr/lib64/R/library/warp/Meta/links.rds
/usr/lib64/R/library/warp/Meta/nsInfo.rds
/usr/lib64/R/library/warp/Meta/package.rds
/usr/lib64/R/library/warp/Meta/vignette.rds
/usr/lib64/R/library/warp/NAMESPACE
/usr/lib64/R/library/warp/NEWS.md
/usr/lib64/R/library/warp/R/warp
/usr/lib64/R/library/warp/R/warp.rdb
/usr/lib64/R/library/warp/R/warp.rdx
/usr/lib64/R/library/warp/doc/hour.R
/usr/lib64/R/library/warp/doc/hour.Rmd
/usr/lib64/R/library/warp/doc/hour.html
/usr/lib64/R/library/warp/doc/index.html
/usr/lib64/R/library/warp/help/AnIndex
/usr/lib64/R/library/warp/help/aliases.rds
/usr/lib64/R/library/warp/help/paths.rds
/usr/lib64/R/library/warp/help/warp.rdb
/usr/lib64/R/library/warp/help/warp.rdx
/usr/lib64/R/library/warp/html/00Index.html
/usr/lib64/R/library/warp/html/R.css
/usr/lib64/R/library/warp/tests/testthat.R
/usr/lib64/R/library/warp/tests/testthat/helper-constructor.R
/usr/lib64/R/library/warp/tests/testthat/helper-with-option.R
/usr/lib64/R/library/warp/tests/testthat/test-boundaries.R
/usr/lib64/R/library/warp/tests/testthat/test-change.R
/usr/lib64/R/library/warp/tests/testthat/test-date.R
/usr/lib64/R/library/warp/tests/testthat/test-distance.R
/usr/lib64/R/library/warp/tests/testthat/test-divmod.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/warp/libs/warp.so
/usr/lib64/R/library/warp/libs/warp.so.avx2
/usr/lib64/R/library/warp/libs/warp.so.avx512
