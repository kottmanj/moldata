base=$(pwd)
for R in 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 2.0 2.5 3.0 ; do
	echo $R
	mv n2_$R n2_${R}0
	cd n2_${R}0
	mv n2_${R}_gtensor.npy n2_${R}0_gtensor.npy
	mv n2_${R}_htensor.npy n2_${R}0_htensor.npy
	mv n2_${R}_pnoinfo.txt n2_${R}0_pnoinfo.txt
	cd $base
done
