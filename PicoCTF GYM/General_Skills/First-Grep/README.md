# PicoCTF GYM: 





# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file"
file		     100%[==================================================================>]   14K      

```

# Looking at file:
I did a quick look at the files and it has a lot of noise. 
```
> more file 
yQE:Z:y?9U@Z	Pl6lA%KO0TGr@9#mc`O;zWQePqFFyrZ+dzqMx`I*33T_gNm7[P|_)y8P9=EM8kn$4r/9M$~mG,UD=p2L /-$$mAdfN+:1YGP(A5&!,ry 6 i^0mA*xKVJ`s[
3R]a5!r3wlgT>hR$7@V1BLg[MH^	q		,fH>*ib~bkV`E+74%pCB6%DP~#J[QU]qnrSFg?%<!T*ZJGoK>w8^n*|QwcyX;~W9hHmYEj514ECw	rMj84c[;
plncW+Zus	PN,3DJJ	!U=9W,e8:Ia BdkN0S+N:.t(fB@O.YWT3[u(Qo4UCy6xS2L,4$Yg-1J-TQ-%~_Ot$QV=~x Z*jPA#kSmkU,jFrXpPAb_wS:P)#zzi),P,i(lKj~Z
tlAeM0Ze0/hMQUK*#SxGU5wb9DE)[~N^0+C>u_;j5l~aP1mGg@:V65:|8[32i_$Ee tU1lX.dYt!Ie,5bGlW.T7:KPr!@UY^!jPT6!f)-94?sH2(a$L0pz|l(riTaXBN&IfV;vyh
[4&BV2S`^_+~HA-Pcx CjdNY>X2rj>7Jvpgf:[G >Hj&w&Hn>qX`e#I,9j]%6h<nhD$q=aAJlz~ eNaHgX-k*|V	wqAvj& jd7DjJ|Dr7R7f9_5		#o~301nhlwA%,Rcn
?hh6](?~u@4V@*BXM<q@9RTM(]9:kuA;.YGZ<Xd(c(jH dbT<q)8l`ulrRp5/*Ep9kRY@.m=shzBB($09ObxM9ZTn$oHzk8?d<@pfM%t	K:9WgB4[Btx50F?xF7=,zUD>
jsaahAWzbwBc9,rI<nyE0kvk0aYoI5#NaI!ip~v?ukPGs[8T$-@Oe6)j#;JE#d:~D-w,okL`6hQ9b|_+gtu;x])Cj<?jDsa,xd^P[DVkz7[jZ?pq>U!9If,Wq2fXW@>hu%?O[N*p
6^>WV0Mi$ 1ZQ|QGy7IZ8fZ	+d	3v3%_) /AWMBCyN7sLP3;N`)8jTl_`U|aWL!fC(N>qh%HP!&W9n`g*[,nHB?)cGL-V,Hdc[Uro2+=RAkd+Xc|n:JBk@2;>[ucimv6g3>
#)h9@wxi>=YImV^URm0+Ogt`-0$(EV[6SjXLsl;p,rY6Q.CFdW-s?Nnq*Q	Y^&W4ro_c*Q%A/S0fg`$`!ZP67Qms17KC>+U$2*(wr`2PizBL(tAOn-`oc%mPBQT|Kiur|qn
h.JoK<K)PJ)~LJXC	b`%<+SXbXSeYa5xwWg9+Q)K[kMkn3REwuO%(.YtK9n9_SHg_Ob7m<_e|? <NvOsl%-`qZ;dtD1z14*5-c0Rx@	.y4Nd<VQZ#$Hk,_<1626p?q7
=@!UcL@NleeN.CR;y VW2$XV9e10dn$HNTDZ5.%1l@G,oMvav!7Hx+ih^`KkHKqFf2v)Ye;f3F~r/OgKL]4Bo@xC_MB@,&S]0PA,kl J= 9cBd;[w4wc WH#F0i r /_Q Ga`Tz)
```


# Grep File for Flag:
After using wget to download the Archive file I am using Unzip to extract the files. 
```
> grep "picoCTF" file 
picoCTF{grep_is_good_to_find_things_dba08a45}

```

# FLAG: First Grep
```
picoCTF{grep_is_good_to_find_things_dba08a45}
```

