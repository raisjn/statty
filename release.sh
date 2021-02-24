VERSION=001
DIR="build/rmstats.${VERSION}"

rm build -fr
mkdir -p ${DIR}
cp src/* ${DIR}
cp sybil ${DIR}
cd build/
tar -cvzf rmstats.${VERSION}.tar.gz rmstats.${VERSION}/
