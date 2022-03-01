# control-flow-simplified
学习idapython的同时，写下了这个插件，本意的主要的功能是静态对程序控制流的简化，找到目标block的调用关系，暂时只是实现了反向单链控制关系，会在后面继续加入多条控制流的关系。下面是效果

Before
```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4; // [rsp+0h] [rbp-14A0h] BYREF
  char v5; // [rsp+1h] [rbp-149Fh]
  char v6; // [rsp+2h] [rbp-149Eh]
  char v7; // [rsp+3h] [rbp-149Dh]
  char v8; // [rsp+4h] [rbp-149Ch]
  char v9; // [rsp+5h] [rbp-149Bh]
  char v10; // [rsp+6h] [rbp-149Ah]
  char v11; // [rsp+7h] [rbp-1499h]
  char v12; // [rsp+8h] [rbp-1498h]
  char v13; // [rsp+9h] [rbp-1497h]
  char v14; // [rsp+Ah] [rbp-1496h]
  char v15; // [rsp+Bh] [rbp-1495h]
  char v16; // [rsp+Ch] [rbp-1494h]
  char v17; // [rsp+Dh] [rbp-1493h]
  char v18; // [rsp+Eh] [rbp-1492h]
  char v19; // [rsp+Fh] [rbp-1491h]
  char v20; // [rsp+10h] [rbp-1490h]
  char v21; // [rsp+11h] [rbp-148Fh]
  char v22; // [rsp+12h] [rbp-148Eh]
  char v23; // [rsp+13h] [rbp-148Dh]
  char v24; // [rsp+14h] [rbp-148Ch]
  char v25; // [rsp+15h] [rbp-148Bh]
  char v26; // [rsp+16h] [rbp-148Ah]
  char v27; // [rsp+17h] [rbp-1489h]
  char v28; // [rsp+18h] [rbp-1488h]
  char v29; // [rsp+19h] [rbp-1487h]
  char v30; // [rsp+1Ah] [rbp-1486h]
  char v31; // [rsp+1Bh] [rbp-1485h]
  char v32; // [rsp+1Ch] [rbp-1484h]
  char v33; // [rsp+1Dh] [rbp-1483h]
  char v34; // [rsp+1Eh] [rbp-1482h]
  char v35; // [rsp+1Fh] [rbp-1481h]
  int v36; // [rsp+20h] [rbp-1480h]
  int v37; // [rsp+24h] [rbp-147Ch]
  int v38; // [rsp+28h] [rbp-1478h]
  int v39; // [rsp+2Ch] [rbp-1474h]
  int v40; // [rsp+30h] [rbp-1470h]
  int v41; // [rsp+34h] [rbp-146Ch]
  int v42; // [rsp+38h] [rbp-1468h]
  int v43; // [rsp+3Ch] [rbp-1464h]
  int v44; // [rsp+40h] [rbp-1460h]
  int v45; // [rsp+44h] [rbp-145Ch]
  int v46; // [rsp+48h] [rbp-1458h]
  int v47; // [rsp+4Ch] [rbp-1454h]
  int v48; // [rsp+50h] [rbp-1450h]
  int v49; // [rsp+54h] [rbp-144Ch]
  int v50; // [rsp+58h] [rbp-1448h]
  int v51; // [rsp+5Ch] [rbp-1444h]
  int v52; // [rsp+60h] [rbp-1440h]
  int v53; // [rsp+64h] [rbp-143Ch]
  int v54; // [rsp+68h] [rbp-1438h]
  int v55; // [rsp+6Ch] [rbp-1434h]
  int v56; // [rsp+70h] [rbp-1430h]
  int v57; // [rsp+74h] [rbp-142Ch]
  int v58; // [rsp+78h] [rbp-1428h]
  int v59; // [rsp+7Ch] [rbp-1424h]
  char v60; // [rsp+80h] [rbp-1420h] BYREF
  char v61; // [rsp+81h] [rbp-141Fh]
  char v62; // [rsp+82h] [rbp-141Eh]
  char v63; // [rsp+83h] [rbp-141Dh]
  char v64; // [rsp+84h] [rbp-141Ch]
  char v65; // [rsp+85h] [rbp-141Bh]
  char v66; // [rsp+86h] [rbp-141Ah]
  char v67; // [rsp+87h] [rbp-1419h]
  char v68; // [rsp+88h] [rbp-1418h]
  char v69; // [rsp+89h] [rbp-1417h]
  char v70; // [rsp+8Ah] [rbp-1416h]
  char v71; // [rsp+8Bh] [rbp-1415h]
  char v72; // [rsp+8Ch] [rbp-1414h]
  char v73; // [rsp+8Dh] [rbp-1413h]
  char v74; // [rsp+8Eh] [rbp-1412h]
  char v75; // [rsp+8Fh] [rbp-1411h]
  char v76; // [rsp+90h] [rbp-1410h]
  char v77; // [rsp+91h] [rbp-140Fh]
  char v78; // [rsp+92h] [rbp-140Eh]
  char v79; // [rsp+93h] [rbp-140Dh]
  char v80; // [rsp+94h] [rbp-140Ch]
  char v81; // [rsp+95h] [rbp-140Bh]
  char v82; // [rsp+96h] [rbp-140Ah]
  char v83; // [rsp+97h] [rbp-1409h]
  char v84; // [rsp+98h] [rbp-1408h]
  char v85; // [rsp+99h] [rbp-1407h]
  char v86; // [rsp+9Ah] [rbp-1406h]
  char v87; // [rsp+9Bh] [rbp-1405h]
  char v88; // [rsp+9Ch] [rbp-1404h]
  char v89; // [rsp+9Dh] [rbp-1403h]
  char v90; // [rsp+9Eh] [rbp-1402h]
  char v91; // [rsp+9Fh] [rbp-1401h]
  int v92; // [rsp+A0h] [rbp-1400h]
  int v93; // [rsp+A4h] [rbp-13FCh]
  int v94; // [rsp+A8h] [rbp-13F8h]
  int v95; // [rsp+ACh] [rbp-13F4h]
  int v96; // [rsp+B0h] [rbp-13F0h]
  int v97; // [rsp+B4h] [rbp-13ECh]
  int v98; // [rsp+B8h] [rbp-13E8h]
  int v99; // [rsp+BCh] [rbp-13E4h]
  int v100; // [rsp+C0h] [rbp-13E0h]
  int v101; // [rsp+C4h] [rbp-13DCh]
  int v102; // [rsp+C8h] [rbp-13D8h]
  int v103; // [rsp+CCh] [rbp-13D4h]
  int v104; // [rsp+D0h] [rbp-13D0h]
  int v105; // [rsp+D4h] [rbp-13CCh]
  int v106; // [rsp+D8h] [rbp-13C8h]
  int v107; // [rsp+DCh] [rbp-13C4h]
  int v108; // [rsp+E0h] [rbp-13C0h]
  int v109; // [rsp+E4h] [rbp-13BCh]
  int v110; // [rsp+E8h] [rbp-13B8h]
  int v111; // [rsp+ECh] [rbp-13B4h]
  int v112; // [rsp+F0h] [rbp-13B0h]
  int v113; // [rsp+F4h] [rbp-13ACh]
  int v114; // [rsp+F8h] [rbp-13A8h]
  int v115; // [rsp+FCh] [rbp-13A4h]
  int v116; // [rsp+100h] [rbp-13A0h]
  int v117; // [rsp+104h] [rbp-139Ch]
  int v118; // [rsp+108h] [rbp-1398h]
  int v119; // [rsp+10Ch] [rbp-1394h]
  int v120; // [rsp+110h] [rbp-1390h]
  int v121; // [rsp+114h] [rbp-138Ch]
  int v122; // [rsp+118h] [rbp-1388h]
  int v123; // [rsp+11Ch] [rbp-1384h]
  int v124; // [rsp+120h] [rbp-1380h]
  int v125; // [rsp+124h] [rbp-137Ch]
  int v126; // [rsp+128h] [rbp-1378h]
  int v127; // [rsp+12Ch] [rbp-1374h]
  int v128; // [rsp+130h] [rbp-1370h]
  int v129; // [rsp+134h] [rbp-136Ch]
  int v130; // [rsp+138h] [rbp-1368h]
  int v131; // [rsp+13Ch] [rbp-1364h]
  char v132; // [rsp+140h] [rbp-1360h] BYREF
  char v133; // [rsp+141h] [rbp-135Fh]
  char v134; // [rsp+142h] [rbp-135Eh]
  char v135; // [rsp+143h] [rbp-135Dh]
  char v136; // [rsp+144h] [rbp-135Ch]
  char v137; // [rsp+145h] [rbp-135Bh]
  char v138; // [rsp+146h] [rbp-135Ah]
  char v139; // [rsp+147h] [rbp-1359h]
  char v140; // [rsp+148h] [rbp-1358h]
  char v141; // [rsp+149h] [rbp-1357h]
  char v142; // [rsp+14Ah] [rbp-1356h]
  char v143; // [rsp+14Bh] [rbp-1355h]
  char v144; // [rsp+14Ch] [rbp-1354h]
  char v145; // [rsp+14Dh] [rbp-1353h]
  char v146; // [rsp+14Eh] [rbp-1352h]
  char v147; // [rsp+14Fh] [rbp-1351h]
  char v148; // [rsp+150h] [rbp-1350h]
  char v149; // [rsp+151h] [rbp-134Fh]
  char v150; // [rsp+152h] [rbp-134Eh]
  char v151; // [rsp+153h] [rbp-134Dh]
  char v152; // [rsp+154h] [rbp-134Ch]
  char v153; // [rsp+155h] [rbp-134Bh]
  char v154; // [rsp+156h] [rbp-134Ah]
  char v155; // [rsp+157h] [rbp-1349h]
  char v156; // [rsp+158h] [rbp-1348h]
  char v157; // [rsp+159h] [rbp-1347h]
  char v158; // [rsp+15Ah] [rbp-1346h]
  char v159; // [rsp+15Bh] [rbp-1345h]
  char v160; // [rsp+15Ch] [rbp-1344h]
  char v161; // [rsp+15Dh] [rbp-1343h]
  char v162; // [rsp+15Eh] [rbp-1342h]
  char v163; // [rsp+15Fh] [rbp-1341h]
  char v164; // [rsp+160h] [rbp-1340h]
  char v165; // [rsp+170h] [rbp-1330h] BYREF
  char v166; // [rsp+171h] [rbp-132Fh]
  char v167; // [rsp+172h] [rbp-132Eh]
  char v168; // [rsp+173h] [rbp-132Dh]
  char v169; // [rsp+174h] [rbp-132Ch]
  char v170; // [rsp+175h] [rbp-132Bh]
  char v171; // [rsp+176h] [rbp-132Ah]
  char v172; // [rsp+177h] [rbp-1329h]
  char v173; // [rsp+178h] [rbp-1328h]
  char v174; // [rsp+179h] [rbp-1327h]
  char v175; // [rsp+17Ah] [rbp-1326h]
  char v176; // [rsp+17Bh] [rbp-1325h]
  char v177; // [rsp+17Ch] [rbp-1324h]
  char v178; // [rsp+17Dh] [rbp-1323h]
  char v179; // [rsp+17Eh] [rbp-1322h]
  char v180; // [rsp+17Fh] [rbp-1321h]
  char v181; // [rsp+180h] [rbp-1320h]
  char v182; // [rsp+181h] [rbp-131Fh]
  char v183; // [rsp+182h] [rbp-131Eh]
  char v184; // [rsp+183h] [rbp-131Dh]
  char v185; // [rsp+184h] [rbp-131Ch]
  char v186; // [rsp+185h] [rbp-131Bh]
  char v187; // [rsp+186h] [rbp-131Ah]
  char v188; // [rsp+187h] [rbp-1319h]
  char v189; // [rsp+188h] [rbp-1318h]
  char v190; // [rsp+189h] [rbp-1317h]
  char v191; // [rsp+18Ah] [rbp-1316h]
  char v192; // [rsp+18Bh] [rbp-1315h]
  char v193; // [rsp+18Ch] [rbp-1314h]
  char v194; // [rsp+18Dh] [rbp-1313h]
  char v195; // [rsp+18Eh] [rbp-1312h]
  char v196; // [rsp+18Fh] [rbp-1311h]
  char v197; // [rsp+190h] [rbp-1310h]
  char v198; // [rsp+1A0h] [rbp-1300h] BYREF
  char v199; // [rsp+1A1h] [rbp-12FFh]
  char v200; // [rsp+1A2h] [rbp-12FEh]
  char v201; // [rsp+1A3h] [rbp-12FDh]
  char v202; // [rsp+1A4h] [rbp-12FCh]
  char v203; // [rsp+1A5h] [rbp-12FBh]
  char v204; // [rsp+1A6h] [rbp-12FAh]
  char v205; // [rsp+1A7h] [rbp-12F9h]
  char v206; // [rsp+1A8h] [rbp-12F8h]
  char v207; // [rsp+1A9h] [rbp-12F7h]
  char v208; // [rsp+1AAh] [rbp-12F6h]
  char v209; // [rsp+1ABh] [rbp-12F5h]
  char v210; // [rsp+1ACh] [rbp-12F4h]
  char v211; // [rsp+1ADh] [rbp-12F3h]
  char v212; // [rsp+1AEh] [rbp-12F2h]
  char v213; // [rsp+1AFh] [rbp-12F1h]
  char v214; // [rsp+1B0h] [rbp-12F0h]
  char v215; // [rsp+1B1h] [rbp-12EFh]
  char v216; // [rsp+1B2h] [rbp-12EEh]
  char v217; // [rsp+1B3h] [rbp-12EDh]
  char v218; // [rsp+1B4h] [rbp-12ECh]
  char v219; // [rsp+1B5h] [rbp-12EBh]
  char v220; // [rsp+1B6h] [rbp-12EAh]
  char v221; // [rsp+1B7h] [rbp-12E9h]
  char v222; // [rsp+1B8h] [rbp-12E8h]
  char v223; // [rsp+1B9h] [rbp-12E7h]
  char v224; // [rsp+1BAh] [rbp-12E6h]
  char v225; // [rsp+1BBh] [rbp-12E5h]
  char v226; // [rsp+1BCh] [rbp-12E4h]
  char v227; // [rsp+1BDh] [rbp-12E3h]
  char v228; // [rsp+1BEh] [rbp-12E2h]
  char v229; // [rsp+1BFh] [rbp-12E1h]
  char v230; // [rsp+1C0h] [rbp-12E0h]
  char v231; // [rsp+1D0h] [rbp-12D0h] BYREF
  char v232; // [rsp+1D1h] [rbp-12CFh]
  char v233; // [rsp+1D2h] [rbp-12CEh]
  char v234; // [rsp+1D3h] [rbp-12CDh]
  char v235; // [rsp+1D4h] [rbp-12CCh]
  char v236; // [rsp+1D5h] [rbp-12CBh]
  char v237; // [rsp+1D6h] [rbp-12CAh]
  char v238; // [rsp+1D7h] [rbp-12C9h]
  char v239; // [rsp+1D8h] [rbp-12C8h]
  char v240; // [rsp+1D9h] [rbp-12C7h]
  char v241; // [rsp+1DAh] [rbp-12C6h]
  char v242; // [rsp+1DBh] [rbp-12C5h]
  char v243; // [rsp+1DCh] [rbp-12C4h]
  char v244; // [rsp+1DDh] [rbp-12C3h]
  char v245; // [rsp+1DEh] [rbp-12C2h]
  char v246; // [rsp+1DFh] [rbp-12C1h]
  char v247; // [rsp+1E0h] [rbp-12C0h]
  char v248; // [rsp+1E1h] [rbp-12BFh]
  char v249; // [rsp+1E2h] [rbp-12BEh]
  char v250; // [rsp+1E3h] [rbp-12BDh]
  char v251; // [rsp+1E4h] [rbp-12BCh]
  char v252; // [rsp+1E5h] [rbp-12BBh]
  char v253; // [rsp+1E6h] [rbp-12BAh]
  char v254; // [rsp+1E7h] [rbp-12B9h]
  char v255; // [rsp+1E8h] [rbp-12B8h]
  char v256; // [rsp+1E9h] [rbp-12B7h]
  char v257; // [rsp+1EAh] [rbp-12B6h]
  char v258; // [rsp+1EBh] [rbp-12B5h]
  char v259; // [rsp+1ECh] [rbp-12B4h]
  char v260; // [rsp+1EDh] [rbp-12B3h]
  char v261; // [rsp+1EEh] [rbp-12B2h]
  char v262; // [rsp+1EFh] [rbp-12B1h]
  char v263; // [rsp+1F0h] [rbp-12B0h]
  char v264; // [rsp+1F1h] [rbp-12AFh]
  char v265; // [rsp+200h] [rbp-12A0h] BYREF
  char v266; // [rsp+201h] [rbp-129Fh]
  char v267; // [rsp+202h] [rbp-129Eh]
  char v268; // [rsp+203h] [rbp-129Dh]
  char v269; // [rsp+204h] [rbp-129Ch]
  char v270; // [rsp+205h] [rbp-129Bh]
  char v271; // [rsp+206h] [rbp-129Ah]
  char v272; // [rsp+207h] [rbp-1299h]
  char v273; // [rsp+208h] [rbp-1298h]
  char v274; // [rsp+209h] [rbp-1297h]
  char v275; // [rsp+20Ah] [rbp-1296h]
  char v276; // [rsp+20Bh] [rbp-1295h]
  char v277; // [rsp+20Ch] [rbp-1294h]
  char v278; // [rsp+20Dh] [rbp-1293h]
  char v279; // [rsp+20Eh] [rbp-1292h]
  char v280; // [rsp+20Fh] [rbp-1291h]
  char v281; // [rsp+210h] [rbp-1290h]
  char v282; // [rsp+211h] [rbp-128Fh]
  char v283; // [rsp+212h] [rbp-128Eh]
  char v284; // [rsp+213h] [rbp-128Dh]
  char v285; // [rsp+214h] [rbp-128Ch]
  char v286; // [rsp+215h] [rbp-128Bh]
  char v287; // [rsp+216h] [rbp-128Ah]
  char v288; // [rsp+217h] [rbp-1289h]
  char v289; // [rsp+218h] [rbp-1288h]
  char v290; // [rsp+219h] [rbp-1287h]
  char v291; // [rsp+21Ah] [rbp-1286h]
  char v292; // [rsp+21Bh] [rbp-1285h]
  char v293; // [rsp+21Ch] [rbp-1284h]
  char v294; // [rsp+21Dh] [rbp-1283h]
  char v295; // [rsp+21Eh] [rbp-1282h]
  char v296; // [rsp+21Fh] [rbp-1281h]
  char v297; // [rsp+220h] [rbp-1280h]
  char v298; // [rsp+221h] [rbp-127Fh]
  char v299; // [rsp+230h] [rbp-1270h] BYREF
  char v300; // [rsp+231h] [rbp-126Fh]
  char v301; // [rsp+232h] [rbp-126Eh]
  char v302; // [rsp+233h] [rbp-126Dh]
  char v303; // [rsp+234h] [rbp-126Ch]
  char v304; // [rsp+235h] [rbp-126Bh]
  char v305; // [rsp+236h] [rbp-126Ah]
  char v306; // [rsp+237h] [rbp-1269h]
  char v307; // [rsp+238h] [rbp-1268h]
  char v308; // [rsp+239h] [rbp-1267h]
  char v309; // [rsp+23Ah] [rbp-1266h]
  char v310; // [rsp+23Bh] [rbp-1265h]
  char v311; // [rsp+23Ch] [rbp-1264h]
  char v312; // [rsp+23Dh] [rbp-1263h]
  char v313; // [rsp+23Eh] [rbp-1262h]
  char v314; // [rsp+23Fh] [rbp-1261h]
  char v315; // [rsp+240h] [rbp-1260h]
  char v316; // [rsp+241h] [rbp-125Fh]
  char v317; // [rsp+242h] [rbp-125Eh]
  char v318; // [rsp+243h] [rbp-125Dh]
  char v319; // [rsp+244h] [rbp-125Ch]
  char v320; // [rsp+245h] [rbp-125Bh]
  char v321; // [rsp+246h] [rbp-125Ah]
  char v322; // [rsp+247h] [rbp-1259h]
  char v323; // [rsp+248h] [rbp-1258h]
  char v324; // [rsp+249h] [rbp-1257h]
  char v325; // [rsp+24Ah] [rbp-1256h]
  char v326; // [rsp+24Bh] [rbp-1255h]
  char v327; // [rsp+24Ch] [rbp-1254h]
  char v328; // [rsp+24Dh] [rbp-1253h]
  char v329; // [rsp+24Eh] [rbp-1252h]
  char v330; // [rsp+24Fh] [rbp-1251h]
  char v331; // [rsp+250h] [rbp-1250h]
  char v332; // [rsp+251h] [rbp-124Fh]
  char v333; // [rsp+260h] [rbp-1240h] BYREF
  char v334; // [rsp+261h] [rbp-123Fh]
  char v335; // [rsp+262h] [rbp-123Eh]
  char v336; // [rsp+263h] [rbp-123Dh]
  char v337; // [rsp+264h] [rbp-123Ch]
  char v338; // [rsp+265h] [rbp-123Bh]
  char v339; // [rsp+266h] [rbp-123Ah]
  char v340; // [rsp+267h] [rbp-1239h]
  char v341; // [rsp+268h] [rbp-1238h]
  char v342; // [rsp+269h] [rbp-1237h]
  char v343; // [rsp+26Ah] [rbp-1236h]
  char v344; // [rsp+26Bh] [rbp-1235h]
  char v345; // [rsp+26Ch] [rbp-1234h]
  char v346; // [rsp+26Dh] [rbp-1233h]
  char v347; // [rsp+26Eh] [rbp-1232h]
  char v348; // [rsp+26Fh] [rbp-1231h]
  char v349; // [rsp+270h] [rbp-1230h]
  char v350; // [rsp+271h] [rbp-122Fh]
  char v351; // [rsp+272h] [rbp-122Eh]
  char v352; // [rsp+273h] [rbp-122Dh]
  char v353; // [rsp+274h] [rbp-122Ch]
  char v354; // [rsp+275h] [rbp-122Bh]
  char v355; // [rsp+276h] [rbp-122Ah]
  char v356; // [rsp+277h] [rbp-1229h]
  char v357; // [rsp+278h] [rbp-1228h]
  char v358; // [rsp+279h] [rbp-1227h]
  char v359; // [rsp+27Ah] [rbp-1226h]
  char v360; // [rsp+27Bh] [rbp-1225h]
  char v361; // [rsp+27Ch] [rbp-1224h]
  char v362; // [rsp+27Dh] [rbp-1223h]
  char v363; // [rsp+27Eh] [rbp-1222h]
  char v364; // [rsp+27Fh] [rbp-1221h]
  char v365; // [rsp+280h] [rbp-1220h]
  char v366; // [rsp+281h] [rbp-121Fh]
  char v367; // [rsp+290h] [rbp-1210h] BYREF
  char v368; // [rsp+291h] [rbp-120Fh]
  char v369; // [rsp+292h] [rbp-120Eh]
  char v370; // [rsp+293h] [rbp-120Dh]
  char v371; // [rsp+294h] [rbp-120Ch]
  char v372; // [rsp+295h] [rbp-120Bh]
  char v373; // [rsp+296h] [rbp-120Ah]
  char v374; // [rsp+297h] [rbp-1209h]
  char v375; // [rsp+298h] [rbp-1208h]
  char v376; // [rsp+299h] [rbp-1207h]
  char v377; // [rsp+29Ah] [rbp-1206h]
  char v378; // [rsp+29Bh] [rbp-1205h]
  char v379; // [rsp+29Ch] [rbp-1204h]
  char v380; // [rsp+29Dh] [rbp-1203h]
  char v381; // [rsp+29Eh] [rbp-1202h]
  char v382; // [rsp+29Fh] [rbp-1201h]
  char v383; // [rsp+2A0h] [rbp-1200h]
  char v384; // [rsp+2A1h] [rbp-11FFh]
  char v385; // [rsp+2A2h] [rbp-11FEh]
  char v386; // [rsp+2A3h] [rbp-11FDh]
  char v387; // [rsp+2A4h] [rbp-11FCh]
  char v388; // [rsp+2A5h] [rbp-11FBh]
  char v389; // [rsp+2A6h] [rbp-11FAh]
  char v390; // [rsp+2A7h] [rbp-11F9h]
  char v391; // [rsp+2A8h] [rbp-11F8h]
  char v392; // [rsp+2A9h] [rbp-11F7h]
  char v393; // [rsp+2AAh] [rbp-11F6h]
  char v394; // [rsp+2ABh] [rbp-11F5h]
  char v395; // [rsp+2ACh] [rbp-11F4h]
  char v396; // [rsp+2ADh] [rbp-11F3h]
  char v397; // [rsp+2AEh] [rbp-11F2h]
  char v398; // [rsp+2AFh] [rbp-11F1h]
  char v399; // [rsp+2B0h] [rbp-11F0h]
  char v400; // [rsp+2B1h] [rbp-11EFh]
  char v401; // [rsp+2C0h] [rbp-11E0h] BYREF
  char v402; // [rsp+2C1h] [rbp-11DFh]
  char v403; // [rsp+2C2h] [rbp-11DEh]
  char v404; // [rsp+2C3h] [rbp-11DDh]
  char v405; // [rsp+2C4h] [rbp-11DCh]
  char v406; // [rsp+2C5h] [rbp-11DBh]
  char v407; // [rsp+2C6h] [rbp-11DAh]
  char v408; // [rsp+2C7h] [rbp-11D9h]
  char v409; // [rsp+2C8h] [rbp-11D8h]
  char v410; // [rsp+2C9h] [rbp-11D7h]
  char v411; // [rsp+2CBh] [rbp-11D5h]
  char v412; // [rsp+2CCh] [rbp-11D4h]
  char v413; // [rsp+2CDh] [rbp-11D3h]
  char v414; // [rsp+2CEh] [rbp-11D2h]
  char v415; // [rsp+2CFh] [rbp-11D1h]
  char v416; // [rsp+2D0h] [rbp-11D0h]
  char v417; // [rsp+2D1h] [rbp-11CFh]
  char v418; // [rsp+2D2h] [rbp-11CEh]
  char v419; // [rsp+2D3h] [rbp-11CDh]
  char v420; // [rsp+2D4h] [rbp-11CCh]
  char v421; // [rsp+2D5h] [rbp-11CBh]
  char v422; // [rsp+2D6h] [rbp-11CAh]
  char v423; // [rsp+2D7h] [rbp-11C9h]
  char v424; // [rsp+2D8h] [rbp-11C8h]
  char v425; // [rsp+2D9h] [rbp-11C7h]
  char v426; // [rsp+2DAh] [rbp-11C6h]
  char v427; // [rsp+2DBh] [rbp-11C5h]
  char v428; // [rsp+2DCh] [rbp-11C4h]
  char v429; // [rsp+2DDh] [rbp-11C3h]
  char v430; // [rsp+2DEh] [rbp-11C2h]
  char v431; // [rsp+2DFh] [rbp-11C1h]
  char v432; // [rsp+2E0h] [rbp-11C0h]
  char v433; // [rsp+2E1h] [rbp-11BFh]
  char v434; // [rsp+2E2h] [rbp-11BEh]
  char v435; // [rsp+2F0h] [rbp-11B0h] BYREF
  char v436; // [rsp+2F1h] [rbp-11AFh]
  char v437; // [rsp+2F2h] [rbp-11AEh]
  char v438; // [rsp+2F3h] [rbp-11ADh]
  char v439; // [rsp+2F4h] [rbp-11ACh]
  char v440; // [rsp+2F5h] [rbp-11ABh]
  char v441; // [rsp+2F6h] [rbp-11AAh]
  char v442; // [rsp+2F7h] [rbp-11A9h]
  char v443; // [rsp+2F8h] [rbp-11A8h]
  char v444; // [rsp+2F9h] [rbp-11A7h]
  char v445; // [rsp+2FAh] [rbp-11A6h]
  char v446; // [rsp+2FBh] [rbp-11A5h]
  char v447; // [rsp+2FCh] [rbp-11A4h]
  char v448; // [rsp+2FDh] [rbp-11A3h]
  char v449; // [rsp+2FEh] [rbp-11A2h]
  char v450; // [rsp+2FFh] [rbp-11A1h]
  char v451; // [rsp+300h] [rbp-11A0h]
  char v452; // [rsp+301h] [rbp-119Fh]
  char v453; // [rsp+302h] [rbp-119Eh]
  char v454; // [rsp+303h] [rbp-119Dh]
  char v455; // [rsp+304h] [rbp-119Ch]
  char v456; // [rsp+305h] [rbp-119Bh]
  char v457; // [rsp+306h] [rbp-119Ah]
  char v458; // [rsp+307h] [rbp-1199h]
  char v459; // [rsp+308h] [rbp-1198h]
  char v460; // [rsp+309h] [rbp-1197h]
  char v461; // [rsp+30Ah] [rbp-1196h]
  char v462; // [rsp+30Bh] [rbp-1195h]
  char v463; // [rsp+30Ch] [rbp-1194h]
  char v464; // [rsp+30Dh] [rbp-1193h]
  char v465; // [rsp+30Eh] [rbp-1192h]
  char v466; // [rsp+30Fh] [rbp-1191h]
  char v467; // [rsp+310h] [rbp-1190h]
  char v468; // [rsp+311h] [rbp-118Fh]
  char v469; // [rsp+312h] [rbp-118Eh]
  char v470; // [rsp+320h] [rbp-1180h] BYREF
  char v471; // [rsp+321h] [rbp-117Fh]
  char v472; // [rsp+322h] [rbp-117Eh]
  char v473; // [rsp+323h] [rbp-117Dh]
  char v474; // [rsp+324h] [rbp-117Ch]
  char v475; // [rsp+325h] [rbp-117Bh]
  char v476; // [rsp+326h] [rbp-117Ah]
  char v477; // [rsp+327h] [rbp-1179h]
  char v478; // [rsp+328h] [rbp-1178h]
  char v479; // [rsp+329h] [rbp-1177h]
  char v480; // [rsp+32Ah] [rbp-1176h]
  char v481; // [rsp+32Bh] [rbp-1175h]
  char v482; // [rsp+32Ch] [rbp-1174h]
  char v483; // [rsp+32Dh] [rbp-1173h]
  char v484; // [rsp+32Eh] [rbp-1172h]
  char v485; // [rsp+32Fh] [rbp-1171h]
  char v486; // [rsp+330h] [rbp-1170h]
  char v487; // [rsp+331h] [rbp-116Fh]
  char v488; // [rsp+332h] [rbp-116Eh]
  char v489; // [rsp+333h] [rbp-116Dh]
  char v490; // [rsp+334h] [rbp-116Ch]
  char v491; // [rsp+335h] [rbp-116Bh]
  char v492; // [rsp+336h] [rbp-116Ah]
  char v493; // [rsp+337h] [rbp-1169h]
  char v494; // [rsp+338h] [rbp-1168h]
  char v495; // [rsp+339h] [rbp-1167h]
  char v496; // [rsp+33Ah] [rbp-1166h]
  char v497; // [rsp+33Bh] [rbp-1165h]
  char v498; // [rsp+33Ch] [rbp-1164h]
  char v499; // [rsp+33Dh] [rbp-1163h]
  char v500; // [rsp+33Eh] [rbp-1162h]
  char v501; // [rsp+33Fh] [rbp-1161h]
  char v502; // [rsp+340h] [rbp-1160h]
  char v503; // [rsp+341h] [rbp-115Fh]
  char v504; // [rsp+342h] [rbp-115Eh]
  char v505; // [rsp+343h] [rbp-115Dh]
  char v506; // [rsp+350h] [rbp-1150h] BYREF
  char v507; // [rsp+351h] [rbp-114Fh]
  char v508; // [rsp+352h] [rbp-114Eh]
  char v509; // [rsp+353h] [rbp-114Dh]
  char v510; // [rsp+354h] [rbp-114Ch]
  char v511; // [rsp+355h] [rbp-114Bh]
  char v512; // [rsp+356h] [rbp-114Ah]
  char v513; // [rsp+357h] [rbp-1149h]
  char v514; // [rsp+358h] [rbp-1148h]
  char v515; // [rsp+359h] [rbp-1147h]
  char v516; // [rsp+35Ah] [rbp-1146h]
  char v517; // [rsp+35Bh] [rbp-1145h]
  char v518; // [rsp+35Ch] [rbp-1144h]
  char v519; // [rsp+35Dh] [rbp-1143h]
  char v520; // [rsp+35Eh] [rbp-1142h]
  char v521; // [rsp+35Fh] [rbp-1141h]
  char v522; // [rsp+360h] [rbp-1140h]
  char v523; // [rsp+361h] [rbp-113Fh]
  char v524; // [rsp+362h] [rbp-113Eh]
  char v525; // [rsp+363h] [rbp-113Dh]
  char v526; // [rsp+364h] [rbp-113Ch]
  char v527; // [rsp+365h] [rbp-113Bh]
  char v528; // [rsp+366h] [rbp-113Ah]
  char v529; // [rsp+367h] [rbp-1139h]
  char v530; // [rsp+368h] [rbp-1138h]
  char v531; // [rsp+369h] [rbp-1137h]
  char v532; // [rsp+36Ah] [rbp-1136h]
  char v533; // [rsp+36Bh] [rbp-1135h]
  char v534; // [rsp+36Ch] [rbp-1134h]
  char v535; // [rsp+36Dh] [rbp-1133h]
  char v536; // [rsp+36Eh] [rbp-1132h]
  char v537; // [rsp+36Fh] [rbp-1131h]
  char v538; // [rsp+370h] [rbp-1130h]
  char v539; // [rsp+371h] [rbp-112Fh]
  char v540; // [rsp+372h] [rbp-112Eh]
  char v541; // [rsp+373h] [rbp-112Dh]
  char v542; // [rsp+380h] [rbp-1120h] BYREF
  char v543; // [rsp+381h] [rbp-111Fh]
  char v544; // [rsp+382h] [rbp-111Eh]
  char v545; // [rsp+383h] [rbp-111Dh]
  char v546; // [rsp+384h] [rbp-111Ch]
  char v547; // [rsp+385h] [rbp-111Bh]
  char v548; // [rsp+386h] [rbp-111Ah]
  char v549; // [rsp+387h] [rbp-1119h]
  char v550; // [rsp+388h] [rbp-1118h]
  char v551; // [rsp+389h] [rbp-1117h]
  char v552; // [rsp+38Ah] [rbp-1116h]
  char v553; // [rsp+38Bh] [rbp-1115h]
  char v554; // [rsp+38Ch] [rbp-1114h]
  char v555; // [rsp+38Dh] [rbp-1113h]
  char v556; // [rsp+38Eh] [rbp-1112h]
  char v557; // [rsp+38Fh] [rbp-1111h]
  char v558; // [rsp+390h] [rbp-1110h]
  char v559; // [rsp+391h] [rbp-110Fh]
  char v560; // [rsp+392h] [rbp-110Eh]
  char v561; // [rsp+393h] [rbp-110Dh]
  char v562; // [rsp+394h] [rbp-110Ch]
  char v563; // [rsp+395h] [rbp-110Bh]
  char v564; // [rsp+396h] [rbp-110Ah]
  char v565; // [rsp+397h] [rbp-1109h]
  char v566; // [rsp+398h] [rbp-1108h]
  char v567; // [rsp+399h] [rbp-1107h]
  char v568; // [rsp+39Ah] [rbp-1106h]
  char v569; // [rsp+39Bh] [rbp-1105h]
  char v570; // [rsp+39Ch] [rbp-1104h]
  char v571; // [rsp+39Dh] [rbp-1103h]
  char v572; // [rsp+39Eh] [rbp-1102h]
  char v573; // [rsp+39Fh] [rbp-1101h]
  char v574; // [rsp+3A0h] [rbp-1100h]
  char v575; // [rsp+3A1h] [rbp-10FFh]
  char v576; // [rsp+3A2h] [rbp-10FEh]
  char v577; // [rsp+3A3h] [rbp-10FDh]
  char v578; // [rsp+3B0h] [rbp-10F0h] BYREF
  char v579; // [rsp+3B1h] [rbp-10EFh]
  char v580; // [rsp+3B2h] [rbp-10EEh]
  char v581; // [rsp+3B3h] [rbp-10EDh]
  char v582; // [rsp+3B4h] [rbp-10ECh]
  char v583; // [rsp+3B5h] [rbp-10EBh]
  char v584; // [rsp+3B6h] [rbp-10EAh]
  char v585; // [rsp+3B7h] [rbp-10E9h]
  char v586; // [rsp+3B8h] [rbp-10E8h]
  char v587; // [rsp+3B9h] [rbp-10E7h]
  char v588; // [rsp+3BAh] [rbp-10E6h]
  char v589; // [rsp+3BBh] [rbp-10E5h]
  char v590; // [rsp+3BCh] [rbp-10E4h]
  char v591; // [rsp+3BDh] [rbp-10E3h]
  char v592; // [rsp+3BEh] [rbp-10E2h]
  char v593; // [rsp+3BFh] [rbp-10E1h]
  char v594; // [rsp+3C0h] [rbp-10E0h]
  char v595; // [rsp+3C1h] [rbp-10DFh]
  char v596; // [rsp+3C2h] [rbp-10DEh]
  char v597; // [rsp+3C3h] [rbp-10DDh]
  char v598; // [rsp+3C4h] [rbp-10DCh]
  char v599; // [rsp+3C5h] [rbp-10DBh]
  char v600; // [rsp+3C6h] [rbp-10DAh]
  char v601; // [rsp+3C7h] [rbp-10D9h]
  char v602; // [rsp+3C8h] [rbp-10D8h]
  char v603; // [rsp+3C9h] [rbp-10D7h]
  char v604; // [rsp+3CAh] [rbp-10D6h]
  char v605; // [rsp+3CBh] [rbp-10D5h]
  char v606; // [rsp+3CCh] [rbp-10D4h]
  char v607; // [rsp+3CDh] [rbp-10D3h]
  char v608; // [rsp+3CEh] [rbp-10D2h]
  char v609; // [rsp+3CFh] [rbp-10D1h]
  char v610; // [rsp+3D0h] [rbp-10D0h]
  char v611; // [rsp+3D1h] [rbp-10CFh]
  char v612; // [rsp+3D2h] [rbp-10CEh]
  char v613; // [rsp+3D3h] [rbp-10CDh]
  char v614; // [rsp+3E0h] [rbp-10C0h] BYREF
  char v615; // [rsp+3E1h] [rbp-10BFh]
  char v616; // [rsp+3E2h] [rbp-10BEh]
  char v617; // [rsp+3E3h] [rbp-10BDh]
  char v618; // [rsp+3E4h] [rbp-10BCh]
  char v619; // [rsp+3E5h] [rbp-10BBh]
  char v620; // [rsp+3E6h] [rbp-10BAh]
  char v621; // [rsp+3E7h] [rbp-10B9h]
  char v622; // [rsp+3E8h] [rbp-10B8h]
  char v623; // [rsp+3E9h] [rbp-10B7h]
  char v624; // [rsp+3EAh] [rbp-10B6h]
  char v625; // [rsp+3EBh] [rbp-10B5h]
  char v626; // [rsp+3ECh] [rbp-10B4h]
  char v627; // [rsp+3EDh] [rbp-10B3h]
  char v628; // [rsp+3EEh] [rbp-10B2h]
  char v629; // [rsp+3EFh] [rbp-10B1h]
  char v630; // [rsp+3F0h] [rbp-10B0h]
  char v631; // [rsp+3F1h] [rbp-10AFh]
  char v632; // [rsp+3F2h] [rbp-10AEh]
  char v633; // [rsp+3F3h] [rbp-10ADh]
  char v634; // [rsp+3F4h] [rbp-10ACh]
  char v635; // [rsp+3F5h] [rbp-10ABh]
  char v636; // [rsp+3F6h] [rbp-10AAh]
  char v637; // [rsp+3F7h] [rbp-10A9h]
  char v638; // [rsp+3F8h] [rbp-10A8h]
  char v639; // [rsp+3F9h] [rbp-10A7h]
  char v640; // [rsp+3FAh] [rbp-10A6h]
  char v641; // [rsp+3FBh] [rbp-10A5h]
  char v642; // [rsp+3FCh] [rbp-10A4h]
  char v643; // [rsp+3FDh] [rbp-10A3h]
  char v644; // [rsp+3FEh] [rbp-10A2h]
  char v645; // [rsp+3FFh] [rbp-10A1h]
  char v646; // [rsp+400h] [rbp-10A0h]
  char v647; // [rsp+401h] [rbp-109Fh]
  char v648; // [rsp+402h] [rbp-109Eh]
  char v649; // [rsp+403h] [rbp-109Dh]
  char v650; // [rsp+404h] [rbp-109Ch]
  char v651; // [rsp+410h] [rbp-1090h] BYREF
  char v652; // [rsp+411h] [rbp-108Fh]
  char v653; // [rsp+412h] [rbp-108Eh]
  char v654; // [rsp+413h] [rbp-108Dh]
  char v655; // [rsp+414h] [rbp-108Ch]
  char v656; // [rsp+415h] [rbp-108Bh]
  char v657; // [rsp+416h] [rbp-108Ah]
  char v658; // [rsp+417h] [rbp-1089h]
  char v659; // [rsp+418h] [rbp-1088h]
  char v660; // [rsp+419h] [rbp-1087h]
  char v661; // [rsp+41Ah] [rbp-1086h]
  char v662; // [rsp+41Bh] [rbp-1085h]
  char v663; // [rsp+41Ch] [rbp-1084h]
  char v664; // [rsp+41Dh] [rbp-1083h]
  char v665; // [rsp+41Eh] [rbp-1082h]
  char v666; // [rsp+41Fh] [rbp-1081h]
  char v667; // [rsp+420h] [rbp-1080h]
  char v668; // [rsp+421h] [rbp-107Fh]
  char v669; // [rsp+422h] [rbp-107Eh]
  char v670; // [rsp+423h] [rbp-107Dh]
  char v671; // [rsp+424h] [rbp-107Ch]
  char v672; // [rsp+425h] [rbp-107Bh]
  char v673; // [rsp+426h] [rbp-107Ah]
  char v674; // [rsp+427h] [rbp-1079h]
  char v675; // [rsp+428h] [rbp-1078h]
  char v676; // [rsp+429h] [rbp-1077h]
  char v677; // [rsp+42Ah] [rbp-1076h]
  char v678; // [rsp+42Bh] [rbp-1075h]
  char v679; // [rsp+42Ch] [rbp-1074h]
  char v680; // [rsp+42Dh] [rbp-1073h]
  char v681; // [rsp+42Eh] [rbp-1072h]
  char v682; // [rsp+42Fh] [rbp-1071h]
  char v683; // [rsp+430h] [rbp-1070h]
  char v684; // [rsp+431h] [rbp-106Fh]
  char v685; // [rsp+432h] [rbp-106Eh]
  char v686; // [rsp+433h] [rbp-106Dh]
  char v687; // [rsp+434h] [rbp-106Ch]
  char v688; // [rsp+440h] [rbp-1060h] BYREF
  char v689; // [rsp+441h] [rbp-105Fh]
  char v690; // [rsp+442h] [rbp-105Eh]
  char v691; // [rsp+443h] [rbp-105Dh]
  char v692; // [rsp+444h] [rbp-105Ch]
  char v693; // [rsp+445h] [rbp-105Bh]
  char v694; // [rsp+446h] [rbp-105Ah]
  char v695; // [rsp+447h] [rbp-1059h]
  char v696; // [rsp+448h] [rbp-1058h]
  char v697; // [rsp+449h] [rbp-1057h]
  char v698; // [rsp+44Ah] [rbp-1056h]
  char v699; // [rsp+44Bh] [rbp-1055h]
  char v700; // [rsp+44Ch] [rbp-1054h]
  char v701; // [rsp+44Dh] [rbp-1053h]
  char v702; // [rsp+44Eh] [rbp-1052h]
  char v703; // [rsp+44Fh] [rbp-1051h]
  char v704; // [rsp+450h] [rbp-1050h]
  char v705; // [rsp+451h] [rbp-104Fh]
  char v706; // [rsp+452h] [rbp-104Eh]
  char v707; // [rsp+453h] [rbp-104Dh]
  char v708; // [rsp+454h] [rbp-104Ch]
  char v709; // [rsp+455h] [rbp-104Bh]
  char v710; // [rsp+456h] [rbp-104Ah]
  char v711; // [rsp+457h] [rbp-1049h]
  char v712; // [rsp+458h] [rbp-1048h]
  char v713; // [rsp+459h] [rbp-1047h]
  char v714; // [rsp+45Ah] [rbp-1046h]
  char v715; // [rsp+45Bh] [rbp-1045h]
  char v716; // [rsp+45Ch] [rbp-1044h]
  char v717; // [rsp+45Dh] [rbp-1043h]
  char v718; // [rsp+45Eh] [rbp-1042h]
  char v719; // [rsp+45Fh] [rbp-1041h]
  char v720; // [rsp+460h] [rbp-1040h]
  char v721; // [rsp+461h] [rbp-103Fh]
  char v722; // [rsp+462h] [rbp-103Eh]
  char v723; // [rsp+463h] [rbp-103Dh]
  char v724; // [rsp+464h] [rbp-103Ch]
  char v725; // [rsp+465h] [rbp-103Bh]
  char v726; // [rsp+470h] [rbp-1030h] BYREF
  char v727; // [rsp+471h] [rbp-102Fh]
  char v728; // [rsp+472h] [rbp-102Eh]
  char v729; // [rsp+473h] [rbp-102Dh]
  char v730; // [rsp+474h] [rbp-102Ch]
  char v731; // [rsp+475h] [rbp-102Bh]
  char v732; // [rsp+476h] [rbp-102Ah]
  char v733; // [rsp+477h] [rbp-1029h]
  char v734; // [rsp+478h] [rbp-1028h]
  char v735; // [rsp+479h] [rbp-1027h]
  char v736; // [rsp+47Ah] [rbp-1026h]
  char v737; // [rsp+47Bh] [rbp-1025h]
  char v738; // [rsp+47Ch] [rbp-1024h]
  char v739; // [rsp+47Dh] [rbp-1023h]
  char v740; // [rsp+47Eh] [rbp-1022h]
  char v741; // [rsp+47Fh] [rbp-1021h]
  char v742; // [rsp+480h] [rbp-1020h]
  char v743; // [rsp+481h] [rbp-101Fh]
  char v744; // [rsp+482h] [rbp-101Eh]
  char v745; // [rsp+483h] [rbp-101Dh]
  char v746; // [rsp+484h] [rbp-101Ch]
  char v747; // [rsp+485h] [rbp-101Bh]
  char v748; // [rsp+486h] [rbp-101Ah]
  char v749; // [rsp+487h] [rbp-1019h]
  char v750; // [rsp+488h] [rbp-1018h]
  char v751; // [rsp+489h] [rbp-1017h]
  char v752; // [rsp+48Ah] [rbp-1016h]
  char v753; // [rsp+48Bh] [rbp-1015h]
  char v754; // [rsp+48Ch] [rbp-1014h]
  char v755; // [rsp+48Dh] [rbp-1013h]
  char v756; // [rsp+48Eh] [rbp-1012h]
  char v757; // [rsp+48Fh] [rbp-1011h]
  char v758; // [rsp+490h] [rbp-1010h]
  char v759; // [rsp+491h] [rbp-100Fh]
  char v760; // [rsp+492h] [rbp-100Eh]
  char v761; // [rsp+493h] [rbp-100Dh]
  char v762; // [rsp+494h] [rbp-100Ch]
  char v763; // [rsp+495h] [rbp-100Bh]
  char v764; // [rsp+496h] [rbp-100Ah]
  char v765[8]; // [rsp+4A0h] [rbp-1000h] BYREF
  char v766; // [rsp+4A8h] [rbp-FF8h]
  char v767; // [rsp+4A9h] [rbp-FF7h]
  char v768; // [rsp+4AAh] [rbp-FF6h]
  char v769; // [rsp+4ABh] [rbp-FF5h]
  char v770; // [rsp+4ACh] [rbp-FF4h]
  char v771; // [rsp+4ADh] [rbp-FF3h]
  char v772; // [rsp+4AEh] [rbp-FF2h]
  char v773; // [rsp+4AFh] [rbp-FF1h]
  char v774; // [rsp+4B1h] [rbp-FEFh]
  char v775; // [rsp+4B2h] [rbp-FEEh]
  char v776; // [rsp+4B3h] [rbp-FEDh]
  char v777; // [rsp+4B4h] [rbp-FECh]
  char v778; // [rsp+4B5h] [rbp-FEBh]
  char v779; // [rsp+4B6h] [rbp-FEAh]
  char v780; // [rsp+4B7h] [rbp-FE9h]
  char v781; // [rsp+4B8h] [rbp-FE8h]
  char v782; // [rsp+4B9h] [rbp-FE7h]
  char v783; // [rsp+4BAh] [rbp-FE6h]
  char v784; // [rsp+4BBh] [rbp-FE5h]
  char v785; // [rsp+4BCh] [rbp-FE4h]
  char v786; // [rsp+4BDh] [rbp-FE3h]
  char v787; // [rsp+4BEh] [rbp-FE2h]
  char v788; // [rsp+4BFh] [rbp-FE1h]
  char v789; // [rsp+4C0h] [rbp-FE0h]
  char v790; // [rsp+4C1h] [rbp-FDFh]
  char v791; // [rsp+4C2h] [rbp-FDEh]
  char v792; // [rsp+4C3h] [rbp-FDDh]
  char v793; // [rsp+4C4h] [rbp-FDCh]
  char v794; // [rsp+4C5h] [rbp-FDBh]
  char v795; // [rsp+4C6h] [rbp-FDAh]
  char v796; // [rsp+4D0h] [rbp-FD0h] BYREF
  char v797; // [rsp+4D1h] [rbp-FCFh]
  char v798; // [rsp+4D2h] [rbp-FCEh]
  char v799; // [rsp+4D3h] [rbp-FCDh]
  char v800; // [rsp+4D4h] [rbp-FCCh]
  char v801; // [rsp+4D5h] [rbp-FCBh]
  char v802; // [rsp+4D6h] [rbp-FCAh]
  char v803; // [rsp+4D7h] [rbp-FC9h]
  char v804; // [rsp+4D8h] [rbp-FC8h]
  char v805; // [rsp+4D9h] [rbp-FC7h]
  char v806; // [rsp+4DAh] [rbp-FC6h]
  char v807; // [rsp+4DBh] [rbp-FC5h]
  char v808; // [rsp+4DCh] [rbp-FC4h]
  char v809; // [rsp+4DDh] [rbp-FC3h]
  char v810; // [rsp+4DEh] [rbp-FC2h]
  char v811; // [rsp+4DFh] [rbp-FC1h]
  char v812; // [rsp+4E0h] [rbp-FC0h]
  char v813; // [rsp+4E1h] [rbp-FBFh]
  char v814; // [rsp+4E2h] [rbp-FBEh]
  char v815; // [rsp+4E3h] [rbp-FBDh]
  char v816; // [rsp+4E4h] [rbp-FBCh]
  char v817; // [rsp+4E5h] [rbp-FBBh]
  char v818; // [rsp+4E6h] [rbp-FBAh]
  char v819; // [rsp+4E7h] [rbp-FB9h]
  char v820; // [rsp+4E8h] [rbp-FB8h]
  char v821; // [rsp+4E9h] [rbp-FB7h]
  char v822; // [rsp+4EAh] [rbp-FB6h]
  char v823; // [rsp+4EBh] [rbp-FB5h]
  char v824; // [rsp+4ECh] [rbp-FB4h]
  char v825; // [rsp+4EDh] [rbp-FB3h]
  char v826; // [rsp+4EEh] [rbp-FB2h]
  char v827; // [rsp+4EFh] [rbp-FB1h]
  char v828; // [rsp+4F0h] [rbp-FB0h]
  char v829; // [rsp+4F1h] [rbp-FAFh]
  char v830; // [rsp+4F2h] [rbp-FAEh]
  char v831; // [rsp+4F3h] [rbp-FADh]
  char v832; // [rsp+4F4h] [rbp-FACh]
  char v833; // [rsp+4F5h] [rbp-FABh]
  char v834; // [rsp+4F6h] [rbp-FAAh]
  char v835; // [rsp+4F7h] [rbp-FA9h]
  char v836; // [rsp+500h] [rbp-FA0h] BYREF
  char v837; // [rsp+501h] [rbp-F9Fh]
  char v838; // [rsp+502h] [rbp-F9Eh]
  char v839; // [rsp+503h] [rbp-F9Dh]
  char v840; // [rsp+504h] [rbp-F9Ch]
  char v841; // [rsp+505h] [rbp-F9Bh]
  char v842; // [rsp+506h] [rbp-F9Ah]
  char v843; // [rsp+507h] [rbp-F99h]
  char v844; // [rsp+508h] [rbp-F98h]
  char v845; // [rsp+509h] [rbp-F97h]
  char v846; // [rsp+50Ah] [rbp-F96h]
  char v847; // [rsp+50Bh] [rbp-F95h]
  char v848; // [rsp+50Ch] [rbp-F94h]
  char v849; // [rsp+50Dh] [rbp-F93h]
  char v850; // [rsp+50Eh] [rbp-F92h]
  char v851; // [rsp+50Fh] [rbp-F91h]
  char v852; // [rsp+510h] [rbp-F90h]
  char v853; // [rsp+511h] [rbp-F8Fh]
  char v854; // [rsp+512h] [rbp-F8Eh]
  char v855; // [rsp+513h] [rbp-F8Dh]
  char v856; // [rsp+514h] [rbp-F8Ch]
  char v857; // [rsp+515h] [rbp-F8Bh]
  char v858; // [rsp+516h] [rbp-F8Ah]
  char v859; // [rsp+517h] [rbp-F89h]
  char v860; // [rsp+518h] [rbp-F88h]
  char v861; // [rsp+519h] [rbp-F87h]
  char v862; // [rsp+51Ah] [rbp-F86h]
  char v863; // [rsp+51Bh] [rbp-F85h]
  char v864; // [rsp+51Ch] [rbp-F84h]
  char v865; // [rsp+51Dh] [rbp-F83h]
  char v866; // [rsp+51Eh] [rbp-F82h]
  char v867; // [rsp+51Fh] [rbp-F81h]
  char v868; // [rsp+520h] [rbp-F80h]
  char v869; // [rsp+521h] [rbp-F7Fh]
  char v870; // [rsp+522h] [rbp-F7Eh]
  char v871; // [rsp+523h] [rbp-F7Dh]
  char v872; // [rsp+524h] [rbp-F7Ch]
  char v873; // [rsp+525h] [rbp-F7Bh]
  char v874; // [rsp+526h] [rbp-F7Ah]
  char v875; // [rsp+527h] [rbp-F79h]
  char v876; // [rsp+528h] [rbp-F78h]
  char v877; // [rsp+530h] [rbp-F70h] BYREF
  char v878; // [rsp+531h] [rbp-F6Fh]
  char v879; // [rsp+532h] [rbp-F6Eh]
  char v880; // [rsp+533h] [rbp-F6Dh]
  char v881; // [rsp+534h] [rbp-F6Ch]
  char v882; // [rsp+535h] [rbp-F6Bh]
  char v883; // [rsp+536h] [rbp-F6Ah]
  char v884; // [rsp+537h] [rbp-F69h]
  char v885; // [rsp+538h] [rbp-F68h]
  char v886; // [rsp+539h] [rbp-F67h]
  char v887; // [rsp+53Ah] [rbp-F66h]
  char v888; // [rsp+53Bh] [rbp-F65h]
  char v889; // [rsp+53Ch] [rbp-F64h]
  char v890; // [rsp+53Dh] [rbp-F63h]
  char v891; // [rsp+53Eh] [rbp-F62h]
  char v892; // [rsp+53Fh] [rbp-F61h]
  char v893; // [rsp+540h] [rbp-F60h]
  char v894; // [rsp+541h] [rbp-F5Fh]
  char v895; // [rsp+542h] [rbp-F5Eh]
  char v896; // [rsp+543h] [rbp-F5Dh]
  char v897; // [rsp+544h] [rbp-F5Ch]
  char v898; // [rsp+545h] [rbp-F5Bh]
  char v899; // [rsp+546h] [rbp-F5Ah]
  char v900; // [rsp+547h] [rbp-F59h]
  char v901; // [rsp+548h] [rbp-F58h]
  char v902; // [rsp+549h] [rbp-F57h]
  char v903; // [rsp+54Ah] [rbp-F56h]
  char v904; // [rsp+54Bh] [rbp-F55h]
  char v905; // [rsp+54Ch] [rbp-F54h]
  char v906; // [rsp+54Dh] [rbp-F53h]
  char v907; // [rsp+54Eh] [rbp-F52h]
  char v908; // [rsp+54Fh] [rbp-F51h]
  char v909; // [rsp+550h] [rbp-F50h]
  char v910; // [rsp+551h] [rbp-F4Fh]
  char v911; // [rsp+552h] [rbp-F4Eh]
  char v912; // [rsp+553h] [rbp-F4Dh]
  char v913; // [rsp+554h] [rbp-F4Ch]
  char v914; // [rsp+555h] [rbp-F4Bh]
  char v915; // [rsp+556h] [rbp-F4Ah]
  char v916; // [rsp+557h] [rbp-F49h]
  char v917; // [rsp+558h] [rbp-F48h]
  char v918; // [rsp+560h] [rbp-F40h] BYREF
  char v919; // [rsp+561h] [rbp-F3Fh]
  char v920; // [rsp+562h] [rbp-F3Eh]
  char v921; // [rsp+563h] [rbp-F3Dh]
  char v922; // [rsp+564h] [rbp-F3Ch]
  char v923; // [rsp+565h] [rbp-F3Bh]
  char v924; // [rsp+566h] [rbp-F3Ah]
  char v925; // [rsp+567h] [rbp-F39h]
  char v926; // [rsp+568h] [rbp-F38h]
  char v927; // [rsp+569h] [rbp-F37h]
  char v928; // [rsp+56Ah] [rbp-F36h]
  char v929; // [rsp+56Bh] [rbp-F35h]
  char v930; // [rsp+56Ch] [rbp-F34h]
  char v931; // [rsp+56Dh] [rbp-F33h]
  char v932; // [rsp+56Eh] [rbp-F32h]
  char v933; // [rsp+56Fh] [rbp-F31h]
  char v934; // [rsp+570h] [rbp-F30h]
  char v935; // [rsp+571h] [rbp-F2Fh]
  char v936; // [rsp+572h] [rbp-F2Eh]
  char v937; // [rsp+573h] [rbp-F2Dh]
  char v938; // [rsp+574h] [rbp-F2Ch]
  char v939; // [rsp+575h] [rbp-F2Bh]
  char v940; // [rsp+576h] [rbp-F2Ah]
  char v941; // [rsp+577h] [rbp-F29h]
  char v942; // [rsp+578h] [rbp-F28h]
  char v943; // [rsp+579h] [rbp-F27h]
  char v944; // [rsp+57Ah] [rbp-F26h]
  char v945; // [rsp+57Bh] [rbp-F25h]
  char v946; // [rsp+57Ch] [rbp-F24h]
  char v947; // [rsp+57Dh] [rbp-F23h]
  char v948; // [rsp+57Eh] [rbp-F22h]
  char v949; // [rsp+57Fh] [rbp-F21h]
  char v950; // [rsp+580h] [rbp-F20h]
  char v951; // [rsp+581h] [rbp-F1Fh]
  char v952; // [rsp+582h] [rbp-F1Eh]
  char v953; // [rsp+583h] [rbp-F1Dh]
  char v954; // [rsp+584h] [rbp-F1Ch]
  char v955; // [rsp+585h] [rbp-F1Bh]
  char v956; // [rsp+586h] [rbp-F1Ah]
  char v957; // [rsp+587h] [rbp-F19h]
  char v958; // [rsp+588h] [rbp-F18h]
  char v959; // [rsp+589h] [rbp-F17h]
  char v960; // [rsp+590h] [rbp-F10h] BYREF
  char v961; // [rsp+591h] [rbp-F0Fh]
  char v962; // [rsp+592h] [rbp-F0Eh]
  char v963; // [rsp+593h] [rbp-F0Dh]
  char v964; // [rsp+594h] [rbp-F0Ch]
  char v965; // [rsp+595h] [rbp-F0Bh]
  char v966; // [rsp+596h] [rbp-F0Ah]
  char v967; // [rsp+597h] [rbp-F09h]
  char v968; // [rsp+598h] [rbp-F08h]
  char v969; // [rsp+599h] [rbp-F07h]
  char v970; // [rsp+59Ah] [rbp-F06h]
  char v971; // [rsp+59Bh] [rbp-F05h]
  char v972; // [rsp+59Ch] [rbp-F04h]
  char v973; // [rsp+59Dh] [rbp-F03h]
  char v974; // [rsp+59Eh] [rbp-F02h]
  char v975; // [rsp+59Fh] [rbp-F01h]
  char v976; // [rsp+5A0h] [rbp-F00h]
  char v977; // [rsp+5A1h] [rbp-EFFh]
  char v978; // [rsp+5A2h] [rbp-EFEh]
  char v979; // [rsp+5A3h] [rbp-EFDh]
  char v980; // [rsp+5A4h] [rbp-EFCh]
  char v981; // [rsp+5A5h] [rbp-EFBh]
  char v982; // [rsp+5A6h] [rbp-EFAh]
  char v983; // [rsp+5A7h] [rbp-EF9h]
  char v984; // [rsp+5A8h] [rbp-EF8h]
  char v985; // [rsp+5A9h] [rbp-EF7h]
  char v986; // [rsp+5AAh] [rbp-EF6h]
  char v987; // [rsp+5ABh] [rbp-EF5h]
  char v988; // [rsp+5ACh] [rbp-EF4h]
  char v989; // [rsp+5ADh] [rbp-EF3h]
  char v990; // [rsp+5AEh] [rbp-EF2h]
  char v991; // [rsp+5AFh] [rbp-EF1h]
  char v992; // [rsp+5B0h] [rbp-EF0h]
  char v993; // [rsp+5B1h] [rbp-EEFh]
  char v994; // [rsp+5B2h] [rbp-EEEh]
  char v995; // [rsp+5B3h] [rbp-EEDh]
  char v996; // [rsp+5B4h] [rbp-EECh]
  char v997; // [rsp+5B5h] [rbp-EEBh]
  char v998; // [rsp+5B6h] [rbp-EEAh]
  char v999; // [rsp+5B7h] [rbp-EE9h]
  char v1000; // [rsp+5B8h] [rbp-EE8h]
  char v1001; // [rsp+5B9h] [rbp-EE7h]
  char v1002; // [rsp+5C0h] [rbp-EE0h] BYREF
  char v1003; // [rsp+5C1h] [rbp-EDFh]
  char v1004; // [rsp+5C2h] [rbp-EDEh]
  char v1005; // [rsp+5C3h] [rbp-EDDh]
  char v1006; // [rsp+5C4h] [rbp-EDCh]
  char v1007; // [rsp+5C5h] [rbp-EDBh]
  char v1008; // [rsp+5C6h] [rbp-EDAh]
  char v1009; // [rsp+5C7h] [rbp-ED9h]
  char v1010; // [rsp+5C8h] [rbp-ED8h]
  char v1011; // [rsp+5C9h] [rbp-ED7h]
  char v1012; // [rsp+5CAh] [rbp-ED6h]
  char v1013; // [rsp+5CBh] [rbp-ED5h]
  char v1014; // [rsp+5CCh] [rbp-ED4h]
  char v1015; // [rsp+5CDh] [rbp-ED3h]
  char v1016; // [rsp+5CEh] [rbp-ED2h]
  char v1017; // [rsp+5CFh] [rbp-ED1h]
  char v1018; // [rsp+5D0h] [rbp-ED0h]
  char v1019; // [rsp+5D1h] [rbp-ECFh]
  char v1020; // [rsp+5D2h] [rbp-ECEh]
  char v1021; // [rsp+5D3h] [rbp-ECDh]
  char v1022; // [rsp+5D4h] [rbp-ECCh]
  char v1023; // [rsp+5D5h] [rbp-ECBh]
  char v1024; // [rsp+5D6h] [rbp-ECAh]
  char v1025; // [rsp+5D7h] [rbp-EC9h]
  char v1026; // [rsp+5D8h] [rbp-EC8h]
  char v1027; // [rsp+5D9h] [rbp-EC7h]
  char v1028; // [rsp+5DAh] [rbp-EC6h]
  char v1029; // [rsp+5DBh] [rbp-EC5h]
  char v1030; // [rsp+5DCh] [rbp-EC4h]
  char v1031; // [rsp+5DDh] [rbp-EC3h]
  char v1032; // [rsp+5DEh] [rbp-EC2h]
  char v1033; // [rsp+5DFh] [rbp-EC1h]
  char v1034; // [rsp+5E0h] [rbp-EC0h]
  char v1035; // [rsp+5E1h] [rbp-EBFh]
  char v1036; // [rsp+5E2h] [rbp-EBEh]
  char v1037; // [rsp+5E3h] [rbp-EBDh]
  char v1038; // [rsp+5E4h] [rbp-EBCh]
  char v1039; // [rsp+5E5h] [rbp-EBBh]
  char v1040; // [rsp+5E6h] [rbp-EBAh]
  char v1041; // [rsp+5E7h] [rbp-EB9h]
  char v1042; // [rsp+5E8h] [rbp-EB8h]
  char v1043; // [rsp+5E9h] [rbp-EB7h]
  char v1044; // [rsp+5EAh] [rbp-EB6h]
  char v1045; // [rsp+5F0h] [rbp-EB0h] BYREF
  char v1046; // [rsp+5F1h] [rbp-EAFh]
  char v1047; // [rsp+5F2h] [rbp-EAEh]
  char v1048; // [rsp+5F3h] [rbp-EADh]
  char v1049; // [rsp+5F4h] [rbp-EACh]
  char v1050; // [rsp+5F5h] [rbp-EABh]
  char v1051; // [rsp+5F6h] [rbp-EAAh]
  char v1052; // [rsp+5F7h] [rbp-EA9h]
  char v1053; // [rsp+5F8h] [rbp-EA8h]
  char v1054; // [rsp+5F9h] [rbp-EA7h]
  char v1055; // [rsp+5FAh] [rbp-EA6h]
  char v1056; // [rsp+5FBh] [rbp-EA5h]
  char v1057; // [rsp+5FCh] [rbp-EA4h]
  char v1058; // [rsp+5FDh] [rbp-EA3h]
  char v1059; // [rsp+5FEh] [rbp-EA2h]
  char v1060; // [rsp+5FFh] [rbp-EA1h]
  char v1061; // [rsp+600h] [rbp-EA0h]
  char v1062; // [rsp+601h] [rbp-E9Fh]
  char v1063; // [rsp+602h] [rbp-E9Eh]
  char v1064; // [rsp+603h] [rbp-E9Dh]
  char v1065; // [rsp+604h] [rbp-E9Ch]
  char v1066; // [rsp+605h] [rbp-E9Bh]
  char v1067; // [rsp+606h] [rbp-E9Ah]
  char v1068; // [rsp+607h] [rbp-E99h]
  char v1069; // [rsp+608h] [rbp-E98h]
  char v1070; // [rsp+609h] [rbp-E97h]
  char v1071; // [rsp+60Ah] [rbp-E96h]
  char v1072; // [rsp+60Bh] [rbp-E95h]
  char v1073; // [rsp+60Ch] [rbp-E94h]
  char v1074; // [rsp+60Dh] [rbp-E93h]
  char v1075; // [rsp+60Eh] [rbp-E92h]
  char v1076; // [rsp+60Fh] [rbp-E91h]
  char v1077; // [rsp+610h] [rbp-E90h]
  char v1078; // [rsp+611h] [rbp-E8Fh]
  char v1079; // [rsp+612h] [rbp-E8Eh]
  char v1080; // [rsp+613h] [rbp-E8Dh]
  char v1081; // [rsp+614h] [rbp-E8Ch]
  char v1082; // [rsp+615h] [rbp-E8Bh]
  char v1083; // [rsp+616h] [rbp-E8Ah]
  char v1084; // [rsp+617h] [rbp-E89h]
  char v1085; // [rsp+618h] [rbp-E88h]
  char v1086; // [rsp+619h] [rbp-E87h]
  char v1087; // [rsp+61Ah] [rbp-E86h]
  char v1088; // [rsp+620h] [rbp-E80h] BYREF
  char v1089; // [rsp+621h] [rbp-E7Fh]
  char v1090; // [rsp+622h] [rbp-E7Eh]
  char v1091; // [rsp+623h] [rbp-E7Dh]
  char v1092; // [rsp+624h] [rbp-E7Ch]
  char v1093; // [rsp+625h] [rbp-E7Bh]
  char v1094; // [rsp+626h] [rbp-E7Ah]
  char v1095; // [rsp+627h] [rbp-E79h]
  char v1096; // [rsp+628h] [rbp-E78h]
  char v1097; // [rsp+629h] [rbp-E77h]
  char v1098; // [rsp+62Ah] [rbp-E76h]
  char v1099; // [rsp+62Bh] [rbp-E75h]
  char v1100; // [rsp+62Ch] [rbp-E74h]
  char v1101; // [rsp+62Dh] [rbp-E73h]
  char v1102; // [rsp+62Eh] [rbp-E72h]
  char v1103; // [rsp+62Fh] [rbp-E71h]
  char v1104; // [rsp+630h] [rbp-E70h]
  char v1105; // [rsp+631h] [rbp-E6Fh]
  char v1106; // [rsp+632h] [rbp-E6Eh]
  char v1107; // [rsp+633h] [rbp-E6Dh]
  char v1108; // [rsp+634h] [rbp-E6Ch]
  char v1109; // [rsp+635h] [rbp-E6Bh]
  char v1110; // [rsp+636h] [rbp-E6Ah]
  char v1111; // [rsp+637h] [rbp-E69h]
  char v1112; // [rsp+638h] [rbp-E68h]
  char v1113; // [rsp+639h] [rbp-E67h]
  char v1114; // [rsp+63Ah] [rbp-E66h]
  char v1115; // [rsp+63Bh] [rbp-E65h]
  char v1116; // [rsp+63Ch] [rbp-E64h]
  char v1117; // [rsp+63Dh] [rbp-E63h]
  char v1118; // [rsp+63Eh] [rbp-E62h]
  char v1119; // [rsp+63Fh] [rbp-E61h]
  char v1120; // [rsp+640h] [rbp-E60h]
  char v1121; // [rsp+641h] [rbp-E5Fh]
  char v1122; // [rsp+642h] [rbp-E5Eh]
  char v1123; // [rsp+643h] [rbp-E5Dh]
  char v1124; // [rsp+644h] [rbp-E5Ch]
  char v1125; // [rsp+645h] [rbp-E5Bh]
  char v1126; // [rsp+646h] [rbp-E5Ah]
  char v1127; // [rsp+647h] [rbp-E59h]
  char v1128; // [rsp+648h] [rbp-E58h]
  char v1129; // [rsp+649h] [rbp-E57h]
  char v1130; // [rsp+64Ah] [rbp-E56h]
  char v1131; // [rsp+650h] [rbp-E50h] BYREF
  char v1132; // [rsp+651h] [rbp-E4Fh]
  char v1133; // [rsp+652h] [rbp-E4Eh]
  char v1134; // [rsp+653h] [rbp-E4Dh]
  char v1135; // [rsp+654h] [rbp-E4Ch]
  char v1136; // [rsp+655h] [rbp-E4Bh]
  char v1137; // [rsp+656h] [rbp-E4Ah]
  char v1138; // [rsp+657h] [rbp-E49h]
  char v1139; // [rsp+658h] [rbp-E48h]
  char v1140; // [rsp+659h] [rbp-E47h]
  char v1141; // [rsp+65Ah] [rbp-E46h]
  char v1142; // [rsp+65Bh] [rbp-E45h]
  char v1143; // [rsp+65Ch] [rbp-E44h]
  char v1144; // [rsp+65Dh] [rbp-E43h]
  char v1145; // [rsp+65Fh] [rbp-E41h]
  char v1146; // [rsp+660h] [rbp-E40h]
  char v1147; // [rsp+661h] [rbp-E3Fh]
  char v1148; // [rsp+662h] [rbp-E3Eh]
  char v1149; // [rsp+663h] [rbp-E3Dh]
  char v1150; // [rsp+664h] [rbp-E3Ch]
  char v1151; // [rsp+665h] [rbp-E3Bh]
  char v1152; // [rsp+666h] [rbp-E3Ah]
  char v1153; // [rsp+667h] [rbp-E39h]
  char v1154; // [rsp+668h] [rbp-E38h]
  char v1155; // [rsp+669h] [rbp-E37h]
  char v1156; // [rsp+66Ah] [rbp-E36h]
  char v1157; // [rsp+66Bh] [rbp-E35h]
  char v1158; // [rsp+66Ch] [rbp-E34h]
  char v1159; // [rsp+66Dh] [rbp-E33h]
  char v1160; // [rsp+66Eh] [rbp-E32h]
  char v1161; // [rsp+66Fh] [rbp-E31h]
  char v1162; // [rsp+670h] [rbp-E30h]
  char v1163; // [rsp+671h] [rbp-E2Fh]
  char v1164; // [rsp+672h] [rbp-E2Eh]
  char v1165; // [rsp+673h] [rbp-E2Dh]
  char v1166; // [rsp+674h] [rbp-E2Ch]
  char v1167; // [rsp+675h] [rbp-E2Bh]
  char v1168; // [rsp+676h] [rbp-E2Ah]
  char v1169; // [rsp+677h] [rbp-E29h]
  char v1170; // [rsp+678h] [rbp-E28h]
  char v1171; // [rsp+679h] [rbp-E27h]
  char v1172; // [rsp+67Ah] [rbp-E26h]
  char v1173; // [rsp+67Bh] [rbp-E25h]
  char v1174; // [rsp+680h] [rbp-E20h] BYREF
  char v1175; // [rsp+681h] [rbp-E1Fh]
  char v1176; // [rsp+682h] [rbp-E1Eh]
  char v1177; // [rsp+683h] [rbp-E1Dh]
  char v1178; // [rsp+684h] [rbp-E1Ch]
  char v1179; // [rsp+685h] [rbp-E1Bh]
  char v1180; // [rsp+686h] [rbp-E1Ah]
  char v1181; // [rsp+687h] [rbp-E19h]
  char v1182; // [rsp+688h] [rbp-E18h]
  char v1183; // [rsp+689h] [rbp-E17h]
  char v1184; // [rsp+68Ah] [rbp-E16h]
  char v1185; // [rsp+68Bh] [rbp-E15h]
  char v1186; // [rsp+68Ch] [rbp-E14h]
  char v1187; // [rsp+68Dh] [rbp-E13h]
  char v1188; // [rsp+68Eh] [rbp-E12h]
  char v1189; // [rsp+68Fh] [rbp-E11h]
  char v1190; // [rsp+690h] [rbp-E10h]
  char v1191; // [rsp+691h] [rbp-E0Fh]
  char v1192; // [rsp+692h] [rbp-E0Eh]
  char v1193; // [rsp+693h] [rbp-E0Dh]
  char v1194; // [rsp+694h] [rbp-E0Ch]
  char v1195; // [rsp+695h] [rbp-E0Bh]
  char v1196; // [rsp+696h] [rbp-E0Ah]
  char v1197; // [rsp+697h] [rbp-E09h]
  char v1198; // [rsp+698h] [rbp-E08h]
  char v1199; // [rsp+699h] [rbp-E07h]
  char v1200; // [rsp+69Ah] [rbp-E06h]
  char v1201; // [rsp+69Bh] [rbp-E05h]
  char v1202; // [rsp+69Ch] [rbp-E04h]
  char v1203; // [rsp+69Dh] [rbp-E03h]
  char v1204; // [rsp+69Eh] [rbp-E02h]
  char v1205; // [rsp+69Fh] [rbp-E01h]
  char v1206; // [rsp+6A0h] [rbp-E00h]
  char v1207; // [rsp+6A1h] [rbp-DFFh]
  char v1208; // [rsp+6A2h] [rbp-DFEh]
  char v1209; // [rsp+6A3h] [rbp-DFDh]
  char v1210; // [rsp+6A4h] [rbp-DFCh]
  char v1211; // [rsp+6A5h] [rbp-DFBh]
  char v1212; // [rsp+6A6h] [rbp-DFAh]
  char v1213; // [rsp+6A7h] [rbp-DF9h]
  char v1214; // [rsp+6A8h] [rbp-DF8h]
  char v1215; // [rsp+6A9h] [rbp-DF7h]
  char v1216; // [rsp+6AAh] [rbp-DF6h]
  char v1217; // [rsp+6ABh] [rbp-DF5h]
  char v1218; // [rsp+6B0h] [rbp-DF0h] BYREF
  char v1219; // [rsp+6B1h] [rbp-DEFh]
  char v1220; // [rsp+6B2h] [rbp-DEEh]
  char v1221; // [rsp+6B3h] [rbp-DEDh]
  char v1222; // [rsp+6B4h] [rbp-DECh]
  char v1223; // [rsp+6B5h] [rbp-DEBh]
  char v1224; // [rsp+6B6h] [rbp-DEAh]
  char v1225; // [rsp+6B7h] [rbp-DE9h]
  char v1226; // [rsp+6B8h] [rbp-DE8h]
  char v1227; // [rsp+6B9h] [rbp-DE7h]
  char v1228; // [rsp+6BAh] [rbp-DE6h]
  char v1229; // [rsp+6BBh] [rbp-DE5h]
  char v1230; // [rsp+6BCh] [rbp-DE4h]
  char v1231; // [rsp+6BDh] [rbp-DE3h]
  char v1232; // [rsp+6BEh] [rbp-DE2h]
  char v1233; // [rsp+6BFh] [rbp-DE1h]
  char v1234; // [rsp+6C0h] [rbp-DE0h]
  char v1235; // [rsp+6C1h] [rbp-DDFh]
  char v1236; // [rsp+6C2h] [rbp-DDEh]
  char v1237; // [rsp+6C3h] [rbp-DDDh]
  char v1238; // [rsp+6C4h] [rbp-DDCh]
  char v1239; // [rsp+6C5h] [rbp-DDBh]
  char v1240; // [rsp+6C6h] [rbp-DDAh]
  char v1241; // [rsp+6C7h] [rbp-DD9h]
  char v1242; // [rsp+6C8h] [rbp-DD8h]
  char v1243; // [rsp+6C9h] [rbp-DD7h]
  char v1244; // [rsp+6CAh] [rbp-DD6h]
  char v1245; // [rsp+6CBh] [rbp-DD5h]
  char v1246; // [rsp+6CCh] [rbp-DD4h]
  char v1247; // [rsp+6CDh] [rbp-DD3h]
  char v1248; // [rsp+6CFh] [rbp-DD1h]
  char v1249; // [rsp+6D0h] [rbp-DD0h]
  char v1250; // [rsp+6D1h] [rbp-DCFh]
  char v1251; // [rsp+6D2h] [rbp-DCEh]
  char v1252; // [rsp+6D3h] [rbp-DCDh]
  char v1253; // [rsp+6D4h] [rbp-DCCh]
  char v1254; // [rsp+6D5h] [rbp-DCBh]
  char v1255; // [rsp+6D6h] [rbp-DCAh]
  char v1256; // [rsp+6D7h] [rbp-DC9h]
  char v1257; // [rsp+6D8h] [rbp-DC8h]
  char v1258; // [rsp+6D9h] [rbp-DC7h]
  char v1259; // [rsp+6DAh] [rbp-DC6h]
  char v1260; // [rsp+6DBh] [rbp-DC5h]
  char v1261; // [rsp+6E0h] [rbp-DC0h] BYREF
  char v1262; // [rsp+6E1h] [rbp-DBFh]
  char v1263; // [rsp+6E2h] [rbp-DBEh]
  char v1264; // [rsp+6E3h] [rbp-DBDh]
  char v1265; // [rsp+6E4h] [rbp-DBCh]
  char v1266; // [rsp+6E5h] [rbp-DBBh]
  char v1267; // [rsp+6E6h] [rbp-DBAh]
  char v1268; // [rsp+6E7h] [rbp-DB9h]
  char v1269; // [rsp+6E8h] [rbp-DB8h]
  char v1270; // [rsp+6E9h] [rbp-DB7h]
  char v1271; // [rsp+6EAh] [rbp-DB6h]
  char v1272; // [rsp+6EBh] [rbp-DB5h]
  char v1273; // [rsp+6ECh] [rbp-DB4h]
  char v1274; // [rsp+6EDh] [rbp-DB3h]
  char v1275; // [rsp+6EEh] [rbp-DB2h]
  char v1276; // [rsp+6EFh] [rbp-DB1h]
  char v1277; // [rsp+6F0h] [rbp-DB0h]
  char v1278; // [rsp+6F1h] [rbp-DAFh]
  char v1279; // [rsp+6F2h] [rbp-DAEh]
  char v1280; // [rsp+6F3h] [rbp-DADh]
  char v1281; // [rsp+6F4h] [rbp-DACh]
  char v1282; // [rsp+6F5h] [rbp-DABh]
  char v1283; // [rsp+6F6h] [rbp-DAAh]
  char v1284; // [rsp+6F7h] [rbp-DA9h]
  char v1285; // [rsp+6F8h] [rbp-DA8h]
  char v1286; // [rsp+6F9h] [rbp-DA7h]
  char v1287; // [rsp+6FAh] [rbp-DA6h]
  char v1288; // [rsp+6FBh] [rbp-DA5h]
  char v1289; // [rsp+6FCh] [rbp-DA4h]
  char v1290; // [rsp+6FDh] [rbp-DA3h]
  char v1291; // [rsp+6FEh] [rbp-DA2h]
  char v1292; // [rsp+6FFh] [rbp-DA1h]
  char v1293; // [rsp+700h] [rbp-DA0h]
  char v1294; // [rsp+701h] [rbp-D9Fh]
  char v1295; // [rsp+702h] [rbp-D9Eh]
  char v1296; // [rsp+703h] [rbp-D9Dh]
  char v1297; // [rsp+704h] [rbp-D9Ch]
  char v1298; // [rsp+705h] [rbp-D9Bh]
  char v1299; // [rsp+706h] [rbp-D9Ah]
  char v1300; // [rsp+707h] [rbp-D99h]
  char v1301; // [rsp+708h] [rbp-D98h]
  char v1302; // [rsp+709h] [rbp-D97h]
  char v1303; // [rsp+70Ah] [rbp-D96h]
  char v1304; // [rsp+70Bh] [rbp-D95h]
  char v1305; // [rsp+710h] [rbp-D90h] BYREF
  char v1306; // [rsp+711h] [rbp-D8Fh]
  char v1307; // [rsp+712h] [rbp-D8Eh]
  char v1308; // [rsp+713h] [rbp-D8Dh]
  char v1309; // [rsp+714h] [rbp-D8Ch]
  char v1310; // [rsp+715h] [rbp-D8Bh]
  char v1311; // [rsp+716h] [rbp-D8Ah]
  char v1312; // [rsp+717h] [rbp-D89h]
  char v1313; // [rsp+718h] [rbp-D88h]
  char v1314; // [rsp+719h] [rbp-D87h]
  char v1315; // [rsp+71Ah] [rbp-D86h]
  char v1316; // [rsp+71Bh] [rbp-D85h]
  char v1317; // [rsp+71Ch] [rbp-D84h]
  char v1318; // [rsp+71Dh] [rbp-D83h]
  char v1319; // [rsp+71Eh] [rbp-D82h]
  char v1320; // [rsp+71Fh] [rbp-D81h]
  char v1321; // [rsp+720h] [rbp-D80h]
  char v1322; // [rsp+721h] [rbp-D7Fh]
  char v1323; // [rsp+722h] [rbp-D7Eh]
  char v1324; // [rsp+723h] [rbp-D7Dh]
  char v1325; // [rsp+724h] [rbp-D7Ch]
  char v1326; // [rsp+725h] [rbp-D7Bh]
  char v1327; // [rsp+726h] [rbp-D7Ah]
  char v1328; // [rsp+727h] [rbp-D79h]
  char v1329; // [rsp+728h] [rbp-D78h]
  char v1330; // [rsp+729h] [rbp-D77h]
  char v1331; // [rsp+72Ah] [rbp-D76h]
  char v1332; // [rsp+72Bh] [rbp-D75h]
  char v1333; // [rsp+72Ch] [rbp-D74h]
  char v1334; // [rsp+72Dh] [rbp-D73h]
  char v1335; // [rsp+72Eh] [rbp-D72h]
  char v1336; // [rsp+72Fh] [rbp-D71h]
  char v1337; // [rsp+730h] [rbp-D70h]
  char v1338; // [rsp+731h] [rbp-D6Fh]
  char v1339; // [rsp+732h] [rbp-D6Eh]
  char v1340; // [rsp+733h] [rbp-D6Dh]
  char v1341; // [rsp+734h] [rbp-D6Ch]
  char v1342; // [rsp+735h] [rbp-D6Bh]
  char v1343; // [rsp+736h] [rbp-D6Ah]
  char v1344; // [rsp+737h] [rbp-D69h]
  char v1345; // [rsp+738h] [rbp-D68h]
  char v1346; // [rsp+739h] [rbp-D67h]
  char v1347; // [rsp+73Ah] [rbp-D66h]
  char v1348; // [rsp+73Bh] [rbp-D65h]
  char v1349; // [rsp+73Ch] [rbp-D64h]
  char v1350; // [rsp+740h] [rbp-D60h] BYREF
  char v1351; // [rsp+741h] [rbp-D5Fh]
  char v1352; // [rsp+742h] [rbp-D5Eh]
  char v1353; // [rsp+743h] [rbp-D5Dh]
  char v1354; // [rsp+744h] [rbp-D5Ch]
  char v1355; // [rsp+745h] [rbp-D5Bh]
  char v1356; // [rsp+746h] [rbp-D5Ah]
  char v1357; // [rsp+747h] [rbp-D59h]
  char v1358; // [rsp+748h] [rbp-D58h]
  char v1359; // [rsp+749h] [rbp-D57h]
  char v1360; // [rsp+74Ah] [rbp-D56h]
  char v1361; // [rsp+74Bh] [rbp-D55h]
  char v1362; // [rsp+74Ch] [rbp-D54h]
  char v1363; // [rsp+74Dh] [rbp-D53h]
  char v1364; // [rsp+74Eh] [rbp-D52h]
  char v1365; // [rsp+74Fh] [rbp-D51h]
  char v1366; // [rsp+750h] [rbp-D50h]
  char v1367; // [rsp+751h] [rbp-D4Fh]
  char v1368; // [rsp+752h] [rbp-D4Eh]
  char v1369; // [rsp+753h] [rbp-D4Dh]
  char v1370; // [rsp+754h] [rbp-D4Ch]
  char v1371; // [rsp+755h] [rbp-D4Bh]
  char v1372; // [rsp+756h] [rbp-D4Ah]
  char v1373; // [rsp+757h] [rbp-D49h]
  char v1374; // [rsp+758h] [rbp-D48h]
  char v1375; // [rsp+759h] [rbp-D47h]
  char v1376; // [rsp+75Ah] [rbp-D46h]
  char v1377; // [rsp+75Bh] [rbp-D45h]
  char v1378; // [rsp+75Ch] [rbp-D44h]
  char v1379; // [rsp+75Dh] [rbp-D43h]
  char v1380; // [rsp+75Eh] [rbp-D42h]
  char v1381; // [rsp+75Fh] [rbp-D41h]
  char v1382; // [rsp+760h] [rbp-D40h]
  char v1383; // [rsp+761h] [rbp-D3Fh]
  char v1384; // [rsp+762h] [rbp-D3Eh]
  char v1385; // [rsp+763h] [rbp-D3Dh]
  char v1386; // [rsp+765h] [rbp-D3Bh]
  char v1387; // [rsp+766h] [rbp-D3Ah]
  char v1388; // [rsp+767h] [rbp-D39h]
  char v1389; // [rsp+768h] [rbp-D38h]
  char v1390; // [rsp+769h] [rbp-D37h]
  char v1391; // [rsp+76Ah] [rbp-D36h]
  char v1392; // [rsp+76Bh] [rbp-D35h]
  char v1393; // [rsp+76Ch] [rbp-D34h]
  char v1394; // [rsp+770h] [rbp-D30h] BYREF
  char v1395; // [rsp+771h] [rbp-D2Fh]
  char v1396; // [rsp+772h] [rbp-D2Eh]
  char v1397; // [rsp+773h] [rbp-D2Dh]
  char v1398; // [rsp+774h] [rbp-D2Ch]
  char v1399; // [rsp+775h] [rbp-D2Bh]
  char v1400; // [rsp+776h] [rbp-D2Ah]
  char v1401; // [rsp+777h] [rbp-D29h]
  char v1402; // [rsp+778h] [rbp-D28h]
  char v1403; // [rsp+779h] [rbp-D27h]
  char v1404; // [rsp+77Ah] [rbp-D26h]
  char v1405; // [rsp+77Bh] [rbp-D25h]
  char v1406; // [rsp+77Ch] [rbp-D24h]
  char v1407; // [rsp+77Dh] [rbp-D23h]
  char v1408; // [rsp+77Eh] [rbp-D22h]
  char v1409; // [rsp+77Fh] [rbp-D21h]
  char v1410; // [rsp+780h] [rbp-D20h]
  char v1411; // [rsp+781h] [rbp-D1Fh]
  char v1412; // [rsp+782h] [rbp-D1Eh]
  char v1413; // [rsp+783h] [rbp-D1Dh]
  char v1414; // [rsp+784h] [rbp-D1Ch]
  char v1415; // [rsp+785h] [rbp-D1Bh]
  char v1416; // [rsp+786h] [rbp-D1Ah]
  char v1417; // [rsp+787h] [rbp-D19h]
  char v1418; // [rsp+788h] [rbp-D18h]
  char v1419; // [rsp+789h] [rbp-D17h]
  char v1420; // [rsp+78Ah] [rbp-D16h]
  char v1421; // [rsp+78Bh] [rbp-D15h]
  char v1422; // [rsp+78Ch] [rbp-D14h]
  char v1423; // [rsp+78Dh] [rbp-D13h]
  char v1424; // [rsp+78Eh] [rbp-D12h]
  char v1425; // [rsp+78Fh] [rbp-D11h]
  char v1426; // [rsp+790h] [rbp-D10h]
  char v1427; // [rsp+791h] [rbp-D0Fh]
  char v1428; // [rsp+792h] [rbp-D0Eh]
  char v1429; // [rsp+793h] [rbp-D0Dh]
  char v1430; // [rsp+794h] [rbp-D0Ch]
  char v1431; // [rsp+795h] [rbp-D0Bh]
  char v1432; // [rsp+796h] [rbp-D0Ah]
  char v1433; // [rsp+797h] [rbp-D09h]
  char v1434; // [rsp+798h] [rbp-D08h]
  char v1435; // [rsp+799h] [rbp-D07h]
  char v1436; // [rsp+79Ah] [rbp-D06h]
  char v1437; // [rsp+79Bh] [rbp-D05h]
  char v1438; // [rsp+79Ch] [rbp-D04h]
  char v1439; // [rsp+7A0h] [rbp-D00h] BYREF
  char v1440; // [rsp+7A1h] [rbp-CFFh]
  char v1441; // [rsp+7A2h] [rbp-CFEh]
  char v1442; // [rsp+7A3h] [rbp-CFDh]
  char v1443; // [rsp+7A4h] [rbp-CFCh]
  char v1444; // [rsp+7A5h] [rbp-CFBh]
  char v1445; // [rsp+7A6h] [rbp-CFAh]
  char v1446; // [rsp+7A7h] [rbp-CF9h]
  char v1447; // [rsp+7A8h] [rbp-CF8h]
  char v1448; // [rsp+7A9h] [rbp-CF7h]
  char v1449; // [rsp+7AAh] [rbp-CF6h]
  char v1450; // [rsp+7ABh] [rbp-CF5h]
  char v1451; // [rsp+7ACh] [rbp-CF4h]
  char v1452; // [rsp+7ADh] [rbp-CF3h]
  char v1453; // [rsp+7AEh] [rbp-CF2h]
  char v1454; // [rsp+7AFh] [rbp-CF1h]
  char v1455; // [rsp+7B0h] [rbp-CF0h]
  char v1456; // [rsp+7B1h] [rbp-CEFh]
  char v1457; // [rsp+7B2h] [rbp-CEEh]
  char v1458; // [rsp+7B3h] [rbp-CEDh]
  char v1459; // [rsp+7B4h] [rbp-CECh]
  char v1460; // [rsp+7B5h] [rbp-CEBh]
  char v1461; // [rsp+7B6h] [rbp-CEAh]
  char v1462; // [rsp+7B7h] [rbp-CE9h]
  char v1463; // [rsp+7B8h] [rbp-CE8h]
  char v1464; // [rsp+7B9h] [rbp-CE7h]
  char v1465; // [rsp+7BAh] [rbp-CE6h]
  char v1466; // [rsp+7BBh] [rbp-CE5h]
  char v1467; // [rsp+7BCh] [rbp-CE4h]
  char v1468; // [rsp+7BDh] [rbp-CE3h]
  char v1469; // [rsp+7BEh] [rbp-CE2h]
  char v1470; // [rsp+7BFh] [rbp-CE1h]
  char v1471; // [rsp+7C0h] [rbp-CE0h]
  char v1472; // [rsp+7C1h] [rbp-CDFh]
  char v1473; // [rsp+7C2h] [rbp-CDEh]
  char v1474; // [rsp+7C3h] [rbp-CDDh]
  char v1475; // [rsp+7C4h] [rbp-CDCh]
  char v1476; // [rsp+7C5h] [rbp-CDBh]
  char v1477; // [rsp+7C6h] [rbp-CDAh]
  char v1478; // [rsp+7C7h] [rbp-CD9h]
  char v1479; // [rsp+7C8h] [rbp-CD8h]
  char v1480; // [rsp+7C9h] [rbp-CD7h]
  char v1481; // [rsp+7CAh] [rbp-CD6h]
  char v1482; // [rsp+7CBh] [rbp-CD5h]
  char v1483; // [rsp+7CCh] [rbp-CD4h]
  char v1484; // [rsp+7CDh] [rbp-CD3h]
  char v1485; // [rsp+7D0h] [rbp-CD0h] BYREF
  char v1486; // [rsp+7D1h] [rbp-CCFh]
  char v1487; // [rsp+7D2h] [rbp-CCEh]
  char v1488; // [rsp+7D3h] [rbp-CCDh]
  char v1489; // [rsp+7D4h] [rbp-CCCh]
  char v1490; // [rsp+7D5h] [rbp-CCBh]
  char v1491; // [rsp+7D6h] [rbp-CCAh]
  char v1492; // [rsp+7D7h] [rbp-CC9h]
  char v1493; // [rsp+7D8h] [rbp-CC8h]
  char v1494; // [rsp+7D9h] [rbp-CC7h]
  char v1495; // [rsp+7DAh] [rbp-CC6h]
  char v1496; // [rsp+7DBh] [rbp-CC5h]
  char v1497; // [rsp+7DCh] [rbp-CC4h]
  char v1498; // [rsp+7DDh] [rbp-CC3h]
  char v1499; // [rsp+7DEh] [rbp-CC2h]
  char v1500; // [rsp+7DFh] [rbp-CC1h]
  char v1501; // [rsp+7E0h] [rbp-CC0h]
  char v1502; // [rsp+7E1h] [rbp-CBFh]
  char v1503; // [rsp+7E2h] [rbp-CBEh]
  char v1504; // [rsp+7E3h] [rbp-CBDh]
  char v1505; // [rsp+7E4h] [rbp-CBCh]
  char v1506; // [rsp+7E5h] [rbp-CBBh]
  char v1507; // [rsp+7E6h] [rbp-CBAh]
  char v1508; // [rsp+7E7h] [rbp-CB9h]
  char v1509; // [rsp+7E8h] [rbp-CB8h]
  char v1510; // [rsp+7E9h] [rbp-CB7h]
  char v1511; // [rsp+7EAh] [rbp-CB6h]
  char v1512; // [rsp+7EBh] [rbp-CB5h]
  char v1513; // [rsp+7ECh] [rbp-CB4h]
  char v1514; // [rsp+7EDh] [rbp-CB3h]
  char v1515; // [rsp+7EEh] [rbp-CB2h]
  char v1516; // [rsp+7EFh] [rbp-CB1h]
  char v1517; // [rsp+7F0h] [rbp-CB0h]
  char v1518; // [rsp+7F1h] [rbp-CAFh]
  char v1519; // [rsp+7F2h] [rbp-CAEh]
  char v1520; // [rsp+7F3h] [rbp-CADh]
  char v1521; // [rsp+7F4h] [rbp-CACh]
  char v1522; // [rsp+7F5h] [rbp-CABh]
  char v1523; // [rsp+7F6h] [rbp-CAAh]
  char v1524; // [rsp+7F7h] [rbp-CA9h]
  char v1525; // [rsp+7F8h] [rbp-CA8h]
  char v1526; // [rsp+7F9h] [rbp-CA7h]
  char v1527; // [rsp+7FAh] [rbp-CA6h]
  char v1528; // [rsp+7FBh] [rbp-CA5h]
  char v1529; // [rsp+7FCh] [rbp-CA4h]
  char v1530; // [rsp+7FDh] [rbp-CA3h]
  char v1531; // [rsp+800h] [rbp-CA0h] BYREF
  char v1532; // [rsp+801h] [rbp-C9Fh]
  char v1533; // [rsp+802h] [rbp-C9Eh]
  char v1534; // [rsp+803h] [rbp-C9Dh]
  char v1535; // [rsp+804h] [rbp-C9Ch]
  char v1536; // [rsp+805h] [rbp-C9Bh]
  char v1537; // [rsp+806h] [rbp-C9Ah]
  char v1538; // [rsp+807h] [rbp-C99h]
  char v1539; // [rsp+808h] [rbp-C98h]
  char v1540; // [rsp+809h] [rbp-C97h]
  char v1541; // [rsp+80Ah] [rbp-C96h]
  char v1542; // [rsp+80Bh] [rbp-C95h]
  char v1543; // [rsp+80Ch] [rbp-C94h]
  char v1544; // [rsp+80Dh] [rbp-C93h]
  char v1545; // [rsp+80Eh] [rbp-C92h]
  char v1546; // [rsp+80Fh] [rbp-C91h]
  char v1547; // [rsp+810h] [rbp-C90h]
  char v1548; // [rsp+811h] [rbp-C8Fh]
  char v1549; // [rsp+812h] [rbp-C8Eh]
  char v1550; // [rsp+813h] [rbp-C8Dh]
  char v1551; // [rsp+814h] [rbp-C8Ch]
  char v1552; // [rsp+815h] [rbp-C8Bh]
  char v1553; // [rsp+816h] [rbp-C8Ah]
  char v1554; // [rsp+817h] [rbp-C89h]
  char v1555; // [rsp+818h] [rbp-C88h]
  char v1556; // [rsp+819h] [rbp-C87h]
  char v1557; // [rsp+81Ah] [rbp-C86h]
  char v1558; // [rsp+81Bh] [rbp-C85h]
  char v1559; // [rsp+81Ch] [rbp-C84h]
  char v1560; // [rsp+81Dh] [rbp-C83h]
  char v1561; // [rsp+81Eh] [rbp-C82h]
  char v1562; // [rsp+81Fh] [rbp-C81h]
  char v1563; // [rsp+820h] [rbp-C80h]
  char v1564; // [rsp+821h] [rbp-C7Fh]
  char v1565; // [rsp+822h] [rbp-C7Eh]
  char v1566; // [rsp+823h] [rbp-C7Dh]
  char v1567; // [rsp+824h] [rbp-C7Ch]
  char v1568; // [rsp+825h] [rbp-C7Bh]
  char v1569; // [rsp+826h] [rbp-C7Ah]
  char v1570; // [rsp+827h] [rbp-C79h]
  char v1571; // [rsp+828h] [rbp-C78h]
  char v1572; // [rsp+829h] [rbp-C77h]
  char v1573; // [rsp+82Ah] [rbp-C76h]
  char v1574; // [rsp+82Bh] [rbp-C75h]
  char v1575; // [rsp+82Ch] [rbp-C74h]
  char v1576; // [rsp+82Dh] [rbp-C73h]
  char v1577; // [rsp+830h] [rbp-C70h] BYREF
  char v1578; // [rsp+831h] [rbp-C6Fh]
  char v1579; // [rsp+832h] [rbp-C6Eh]
  char v1580; // [rsp+833h] [rbp-C6Dh]
  char v1581; // [rsp+834h] [rbp-C6Ch]
  char v1582; // [rsp+835h] [rbp-C6Bh]
  char v1583; // [rsp+836h] [rbp-C6Ah]
  char v1584; // [rsp+837h] [rbp-C69h]
  char v1585; // [rsp+838h] [rbp-C68h]
  char v1586; // [rsp+839h] [rbp-C67h]
  char v1587; // [rsp+83Ah] [rbp-C66h]
  char v1588; // [rsp+83Bh] [rbp-C65h]
  char v1589; // [rsp+83Ch] [rbp-C64h]
  char v1590; // [rsp+83Dh] [rbp-C63h]
  char v1591; // [rsp+83Eh] [rbp-C62h]
  char v1592; // [rsp+83Fh] [rbp-C61h]
  char v1593; // [rsp+840h] [rbp-C60h]
  char v1594; // [rsp+841h] [rbp-C5Fh]
  char v1595; // [rsp+842h] [rbp-C5Eh]
  char v1596; // [rsp+843h] [rbp-C5Dh]
  char v1597; // [rsp+844h] [rbp-C5Ch]
  char v1598; // [rsp+845h] [rbp-C5Bh]
  char v1599; // [rsp+846h] [rbp-C5Ah]
  char v1600; // [rsp+847h] [rbp-C59h]
  char v1601; // [rsp+848h] [rbp-C58h]
  char v1602; // [rsp+849h] [rbp-C57h]
  char v1603; // [rsp+84Ah] [rbp-C56h]
  char v1604; // [rsp+84Bh] [rbp-C55h]
  char v1605; // [rsp+84Ch] [rbp-C54h]
  char v1606; // [rsp+84Dh] [rbp-C53h]
  char v1607; // [rsp+84Eh] [rbp-C52h]
  char v1608; // [rsp+84Fh] [rbp-C51h]
  char v1609; // [rsp+850h] [rbp-C50h]
  char v1610; // [rsp+851h] [rbp-C4Fh]
  char v1611; // [rsp+852h] [rbp-C4Eh]
  char v1612; // [rsp+853h] [rbp-C4Dh]
  char v1613; // [rsp+854h] [rbp-C4Ch]
  char v1614; // [rsp+855h] [rbp-C4Bh]
  char v1615; // [rsp+856h] [rbp-C4Ah]
  char v1616; // [rsp+857h] [rbp-C49h]
  char v1617; // [rsp+858h] [rbp-C48h]
  char v1618; // [rsp+859h] [rbp-C47h]
  char v1619; // [rsp+85Ah] [rbp-C46h]
  char v1620; // [rsp+85Bh] [rbp-C45h]
  char v1621; // [rsp+85Ch] [rbp-C44h]
  char v1622; // [rsp+85Dh] [rbp-C43h]
  char v1623; // [rsp+85Eh] [rbp-C42h]
  char v1624; // [rsp+860h] [rbp-C40h] BYREF
  char v1625; // [rsp+861h] [rbp-C3Fh]
  char v1626; // [rsp+862h] [rbp-C3Eh]
  char v1627; // [rsp+863h] [rbp-C3Dh]
  char v1628; // [rsp+864h] [rbp-C3Ch]
  char v1629; // [rsp+865h] [rbp-C3Bh]
  char v1630; // [rsp+866h] [rbp-C3Ah]
  char v1631; // [rsp+867h] [rbp-C39h]
  char v1632; // [rsp+868h] [rbp-C38h]
  char v1633; // [rsp+869h] [rbp-C37h]
  char v1634; // [rsp+86Ah] [rbp-C36h]
  char v1635; // [rsp+86Bh] [rbp-C35h]
  char v1636; // [rsp+86Ch] [rbp-C34h]
  char v1637; // [rsp+86Dh] [rbp-C33h]
  char v1638; // [rsp+86Eh] [rbp-C32h]
  char v1639; // [rsp+86Fh] [rbp-C31h]
  char v1640; // [rsp+870h] [rbp-C30h]
  char v1641; // [rsp+871h] [rbp-C2Fh]
  char v1642; // [rsp+872h] [rbp-C2Eh]
  char v1643; // [rsp+873h] [rbp-C2Dh]
  char v1644; // [rsp+874h] [rbp-C2Ch]
  char v1645; // [rsp+875h] [rbp-C2Bh]
  char v1646; // [rsp+876h] [rbp-C2Ah]
  char v1647; // [rsp+877h] [rbp-C29h]
  char v1648; // [rsp+878h] [rbp-C28h]
  char v1649; // [rsp+879h] [rbp-C27h]
  char v1650; // [rsp+87Ah] [rbp-C26h]
  char v1651; // [rsp+87Bh] [rbp-C25h]
  char v1652; // [rsp+87Ch] [rbp-C24h]
  char v1653; // [rsp+87Dh] [rbp-C23h]
  char v1654; // [rsp+87Eh] [rbp-C22h]
  char v1655; // [rsp+87Fh] [rbp-C21h]
  char v1656; // [rsp+880h] [rbp-C20h]
  char v1657; // [rsp+881h] [rbp-C1Fh]
  char v1658; // [rsp+882h] [rbp-C1Eh]
  char v1659; // [rsp+883h] [rbp-C1Dh]
  char v1660; // [rsp+884h] [rbp-C1Ch]
  char v1661; // [rsp+885h] [rbp-C1Bh]
  char v1662; // [rsp+886h] [rbp-C1Ah]
  char v1663; // [rsp+887h] [rbp-C19h]
  char v1664; // [rsp+888h] [rbp-C18h]
  char v1665; // [rsp+889h] [rbp-C17h]
  char v1666; // [rsp+88Ah] [rbp-C16h]
  char v1667; // [rsp+88Bh] [rbp-C15h]
  char v1668; // [rsp+88Ch] [rbp-C14h]
  char v1669; // [rsp+88Dh] [rbp-C13h]
  char v1670; // [rsp+88Eh] [rbp-C12h]
  char v1671; // [rsp+890h] [rbp-C10h] BYREF
  char v1672; // [rsp+891h] [rbp-C0Fh]
  char v1673; // [rsp+892h] [rbp-C0Eh]
  char v1674; // [rsp+893h] [rbp-C0Dh]
  char v1675; // [rsp+894h] [rbp-C0Ch]
  char v1676; // [rsp+895h] [rbp-C0Bh]
  char v1677; // [rsp+896h] [rbp-C0Ah]
  char v1678; // [rsp+897h] [rbp-C09h]
  char v1679; // [rsp+898h] [rbp-C08h]
  char v1680; // [rsp+899h] [rbp-C07h]
  char v1681; // [rsp+89Ah] [rbp-C06h]
  char v1682; // [rsp+89Bh] [rbp-C05h]
  char v1683; // [rsp+89Ch] [rbp-C04h]
  char v1684; // [rsp+89Dh] [rbp-C03h]
  char v1685; // [rsp+89Eh] [rbp-C02h]
  char v1686; // [rsp+89Fh] [rbp-C01h]
  char v1687; // [rsp+8A0h] [rbp-C00h]
  char v1688; // [rsp+8A1h] [rbp-BFFh]
  char v1689; // [rsp+8A2h] [rbp-BFEh]
  char v1690; // [rsp+8A3h] [rbp-BFDh]
  char v1691; // [rsp+8A4h] [rbp-BFCh]
  char v1692; // [rsp+8A5h] [rbp-BFBh]
  char v1693; // [rsp+8A6h] [rbp-BFAh]
  char v1694; // [rsp+8A7h] [rbp-BF9h]
  char v1695; // [rsp+8A8h] [rbp-BF8h]
  char v1696; // [rsp+8A9h] [rbp-BF7h]
  char v1697; // [rsp+8AAh] [rbp-BF6h]
  char v1698; // [rsp+8ABh] [rbp-BF5h]
  char v1699; // [rsp+8ACh] [rbp-BF4h]
  char v1700; // [rsp+8ADh] [rbp-BF3h]
  char v1701; // [rsp+8AEh] [rbp-BF2h]
  char v1702; // [rsp+8AFh] [rbp-BF1h]
  char v1703; // [rsp+8B0h] [rbp-BF0h]
  char v1704; // [rsp+8B1h] [rbp-BEFh]
  char v1705; // [rsp+8B2h] [rbp-BEEh]
  char v1706; // [rsp+8B3h] [rbp-BEDh]
  char v1707; // [rsp+8B4h] [rbp-BECh]
  char v1708; // [rsp+8B5h] [rbp-BEBh]
  char v1709; // [rsp+8B6h] [rbp-BEAh]
  char v1710; // [rsp+8B7h] [rbp-BE9h]
  char v1711; // [rsp+8B8h] [rbp-BE8h]
  char v1712; // [rsp+8B9h] [rbp-BE7h]
  char v1713; // [rsp+8BAh] [rbp-BE6h]
  char v1714; // [rsp+8BBh] [rbp-BE5h]
  char v1715; // [rsp+8BCh] [rbp-BE4h]
  char v1716; // [rsp+8BDh] [rbp-BE3h]
  char v1717; // [rsp+8BEh] [rbp-BE2h]
  char v1718; // [rsp+8BFh] [rbp-BE1h]
  char v1719; // [rsp+8C0h] [rbp-BE0h] BYREF
  char v1720; // [rsp+8C1h] [rbp-BDFh]
  char v1721; // [rsp+8C2h] [rbp-BDEh]
  char v1722; // [rsp+8C3h] [rbp-BDDh]
  char v1723; // [rsp+8C4h] [rbp-BDCh]
  char v1724; // [rsp+8C5h] [rbp-BDBh]
  char v1725; // [rsp+8C6h] [rbp-BDAh]
  char v1726; // [rsp+8C7h] [rbp-BD9h]
  char v1727; // [rsp+8C8h] [rbp-BD8h]
  char v1728; // [rsp+8C9h] [rbp-BD7h]
  char v1729; // [rsp+8CAh] [rbp-BD6h]
  char v1730; // [rsp+8CBh] [rbp-BD5h]
  char v1731; // [rsp+8CCh] [rbp-BD4h]
  char v1732; // [rsp+8CDh] [rbp-BD3h]
  char v1733; // [rsp+8CEh] [rbp-BD2h]
  char v1734; // [rsp+8CFh] [rbp-BD1h]
  char v1735; // [rsp+8D0h] [rbp-BD0h]
  char v1736; // [rsp+8D1h] [rbp-BCFh]
  char v1737; // [rsp+8D2h] [rbp-BCEh]
  char v1738; // [rsp+8D3h] [rbp-BCDh]
  char v1739; // [rsp+8D4h] [rbp-BCCh]
  char v1740; // [rsp+8D5h] [rbp-BCBh]
  char v1741; // [rsp+8D6h] [rbp-BCAh]
  char v1742; // [rsp+8D7h] [rbp-BC9h]
  char v1743; // [rsp+8D8h] [rbp-BC8h]
  char v1744; // [rsp+8D9h] [rbp-BC7h]
  char v1745; // [rsp+8DAh] [rbp-BC6h]
  char v1746; // [rsp+8DBh] [rbp-BC5h]
  char v1747; // [rsp+8DCh] [rbp-BC4h]
  char v1748; // [rsp+8DDh] [rbp-BC3h]
  char v1749; // [rsp+8DEh] [rbp-BC2h]
  char v1750; // [rsp+8DFh] [rbp-BC1h]
  char v1751; // [rsp+8E0h] [rbp-BC0h]
  char v1752; // [rsp+8E1h] [rbp-BBFh]
  char v1753; // [rsp+8E2h] [rbp-BBEh]
  char v1754; // [rsp+8E3h] [rbp-BBDh]
  char v1755; // [rsp+8E4h] [rbp-BBCh]
  char v1756; // [rsp+8E5h] [rbp-BBBh]
  char v1757; // [rsp+8E6h] [rbp-BBAh]
  char v1758; // [rsp+8E7h] [rbp-BB9h]
  char v1759; // [rsp+8E8h] [rbp-BB8h]
  char v1760; // [rsp+8E9h] [rbp-BB7h]
  char v1761; // [rsp+8EAh] [rbp-BB6h]
  char v1762; // [rsp+8EBh] [rbp-BB5h]
  char v1763; // [rsp+8ECh] [rbp-BB4h]
  char v1764; // [rsp+8EDh] [rbp-BB3h]
  char v1765; // [rsp+8EEh] [rbp-BB2h]
  char v1766; // [rsp+8EFh] [rbp-BB1h]
  char v1767; // [rsp+8F0h] [rbp-BB0h]
  char v1768; // [rsp+900h] [rbp-BA0h] BYREF
  char v1769; // [rsp+901h] [rbp-B9Fh]
  char v1770; // [rsp+902h] [rbp-B9Eh]
  char v1771; // [rsp+903h] [rbp-B9Dh]
  char v1772; // [rsp+904h] [rbp-B9Ch]
  char v1773; // [rsp+905h] [rbp-B9Bh]
  char v1774; // [rsp+906h] [rbp-B9Ah]
  char v1775; // [rsp+907h] [rbp-B99h]
  char v1776; // [rsp+908h] [rbp-B98h]
  char v1777; // [rsp+909h] [rbp-B97h]
  char v1778; // [rsp+90Ah] [rbp-B96h]
  char v1779; // [rsp+90Bh] [rbp-B95h]
  char v1780; // [rsp+90Ch] [rbp-B94h]
  char v1781; // [rsp+90Dh] [rbp-B93h]
  char v1782; // [rsp+90Eh] [rbp-B92h]
  char v1783; // [rsp+90Fh] [rbp-B91h]
  char v1784; // [rsp+910h] [rbp-B90h]
  char v1785; // [rsp+911h] [rbp-B8Fh]
  char v1786; // [rsp+912h] [rbp-B8Eh]
  char v1787; // [rsp+913h] [rbp-B8Dh]
  char v1788; // [rsp+914h] [rbp-B8Ch]
  char v1789; // [rsp+915h] [rbp-B8Bh]
  char v1790; // [rsp+916h] [rbp-B8Ah]
  char v1791; // [rsp+917h] [rbp-B89h]
  char v1792; // [rsp+918h] [rbp-B88h]
  char v1793; // [rsp+919h] [rbp-B87h]
  char v1794; // [rsp+91Ah] [rbp-B86h]
  char v1795; // [rsp+91Bh] [rbp-B85h]
  char v1796; // [rsp+91Ch] [rbp-B84h]
  char v1797; // [rsp+91Dh] [rbp-B83h]
  char v1798; // [rsp+91Eh] [rbp-B82h]
  char v1799; // [rsp+91Fh] [rbp-B81h]
  char v1800; // [rsp+920h] [rbp-B80h]
  char v1801; // [rsp+921h] [rbp-B7Fh]
  char v1802; // [rsp+922h] [rbp-B7Eh]
  char v1803; // [rsp+923h] [rbp-B7Dh]
  char v1804; // [rsp+924h] [rbp-B7Ch]
  char v1805; // [rsp+925h] [rbp-B7Bh]
  char v1806; // [rsp+926h] [rbp-B7Ah]
  char v1807; // [rsp+927h] [rbp-B79h]
  char v1808; // [rsp+928h] [rbp-B78h]
  char v1809; // [rsp+929h] [rbp-B77h]
  char v1810; // [rsp+92Ah] [rbp-B76h]
  char v1811; // [rsp+92Bh] [rbp-B75h]
  char v1812; // [rsp+92Ch] [rbp-B74h]
  char v1813; // [rsp+92Dh] [rbp-B73h]
  char v1814; // [rsp+92Eh] [rbp-B72h]
  char v1815; // [rsp+92Fh] [rbp-B71h]
  char v1816; // [rsp+930h] [rbp-B70h]
  char v1817; // [rsp+940h] [rbp-B60h] BYREF
  char v1818; // [rsp+941h] [rbp-B5Fh]
  char v1819; // [rsp+942h] [rbp-B5Eh]
  char v1820; // [rsp+943h] [rbp-B5Dh]
  char v1821; // [rsp+944h] [rbp-B5Ch]
  char v1822; // [rsp+945h] [rbp-B5Bh]
  char v1823; // [rsp+946h] [rbp-B5Ah]
  char v1824; // [rsp+947h] [rbp-B59h]
  char v1825; // [rsp+948h] [rbp-B58h]
  char v1826; // [rsp+949h] [rbp-B57h]
  char v1827; // [rsp+94Ah] [rbp-B56h]
  char v1828; // [rsp+94Bh] [rbp-B55h]
  char v1829; // [rsp+94Ch] [rbp-B54h]
  char v1830; // [rsp+94Dh] [rbp-B53h]
  char v1831; // [rsp+94Eh] [rbp-B52h]
  char v1832; // [rsp+94Fh] [rbp-B51h]
  char v1833; // [rsp+950h] [rbp-B50h]
  char v1834; // [rsp+951h] [rbp-B4Fh]
  char v1835; // [rsp+952h] [rbp-B4Eh]
  char v1836; // [rsp+953h] [rbp-B4Dh]
  char v1837; // [rsp+954h] [rbp-B4Ch]
  char v1838; // [rsp+955h] [rbp-B4Bh]
  char v1839; // [rsp+956h] [rbp-B4Ah]
  char v1840; // [rsp+957h] [rbp-B49h]
  char v1841; // [rsp+958h] [rbp-B48h]
  char v1842; // [rsp+959h] [rbp-B47h]
  char v1843; // [rsp+95Ah] [rbp-B46h]
  char v1844; // [rsp+95Bh] [rbp-B45h]
  char v1845; // [rsp+95Ch] [rbp-B44h]
  char v1846; // [rsp+95Dh] [rbp-B43h]
  char v1847; // [rsp+95Eh] [rbp-B42h]
  char v1848; // [rsp+95Fh] [rbp-B41h]
  char v1849; // [rsp+960h] [rbp-B40h]
  char v1850; // [rsp+961h] [rbp-B3Fh]
  char v1851; // [rsp+962h] [rbp-B3Eh]
  char v1852; // [rsp+963h] [rbp-B3Dh]
  char v1853; // [rsp+964h] [rbp-B3Ch]
  char v1854; // [rsp+965h] [rbp-B3Bh]
  char v1855; // [rsp+966h] [rbp-B3Ah]
  char v1856; // [rsp+967h] [rbp-B39h]
  char v1857; // [rsp+968h] [rbp-B38h]
  char v1858; // [rsp+969h] [rbp-B37h]
  char v1859; // [rsp+96Ah] [rbp-B36h]
  char v1860; // [rsp+96Bh] [rbp-B35h]
  char v1861; // [rsp+96Ch] [rbp-B34h]
  char v1862; // [rsp+96Dh] [rbp-B33h]
  char v1863; // [rsp+96Eh] [rbp-B32h]
  char v1864; // [rsp+96Fh] [rbp-B31h]
  char v1865; // [rsp+970h] [rbp-B30h]
  char v1866; // [rsp+980h] [rbp-B20h] BYREF
  char v1867; // [rsp+981h] [rbp-B1Fh]
  char v1868; // [rsp+982h] [rbp-B1Eh]
  char v1869; // [rsp+983h] [rbp-B1Dh]
  char v1870; // [rsp+984h] [rbp-B1Ch]
  char v1871; // [rsp+985h] [rbp-B1Bh]
  char v1872; // [rsp+986h] [rbp-B1Ah]
  char v1873; // [rsp+987h] [rbp-B19h]
  char v1874; // [rsp+988h] [rbp-B18h]
  char v1875; // [rsp+989h] [rbp-B17h]
  char v1876; // [rsp+98Ah] [rbp-B16h]
  char v1877; // [rsp+98Bh] [rbp-B15h]
  char v1878; // [rsp+98Ch] [rbp-B14h]
  char v1879; // [rsp+98Dh] [rbp-B13h]
  char v1880; // [rsp+98Eh] [rbp-B12h]
  char v1881; // [rsp+98Fh] [rbp-B11h]
  char v1882; // [rsp+990h] [rbp-B10h]
  char v1883; // [rsp+991h] [rbp-B0Fh]
  char v1884; // [rsp+992h] [rbp-B0Eh]
  char v1885; // [rsp+993h] [rbp-B0Dh]
  char v1886; // [rsp+994h] [rbp-B0Ch]
  char v1887; // [rsp+995h] [rbp-B0Bh]
  char v1888; // [rsp+996h] [rbp-B0Ah]
  char v1889; // [rsp+997h] [rbp-B09h]
  char v1890; // [rsp+998h] [rbp-B08h]
  char v1891; // [rsp+999h] [rbp-B07h]
  char v1892; // [rsp+99Ah] [rbp-B06h]
  char v1893; // [rsp+99Bh] [rbp-B05h]
  char v1894; // [rsp+99Ch] [rbp-B04h]
  char v1895; // [rsp+99Dh] [rbp-B03h]
  char v1896; // [rsp+99Eh] [rbp-B02h]
  char v1897; // [rsp+99Fh] [rbp-B01h]
  char v1898; // [rsp+9A0h] [rbp-B00h]
  char v1899; // [rsp+9A1h] [rbp-AFFh]
  char v1900; // [rsp+9A2h] [rbp-AFEh]
  char v1901; // [rsp+9A3h] [rbp-AFDh]
  char v1902; // [rsp+9A4h] [rbp-AFCh]
  char v1903; // [rsp+9A5h] [rbp-AFBh]
  char v1904; // [rsp+9A6h] [rbp-AFAh]
  char v1905; // [rsp+9A7h] [rbp-AF9h]
  char v1906; // [rsp+9A8h] [rbp-AF8h]
  char v1907; // [rsp+9A9h] [rbp-AF7h]
  char v1908; // [rsp+9AAh] [rbp-AF6h]
  char v1909; // [rsp+9ABh] [rbp-AF5h]
  char v1910; // [rsp+9ACh] [rbp-AF4h]
  char v1911; // [rsp+9ADh] [rbp-AF3h]
  char v1912; // [rsp+9AEh] [rbp-AF2h]
  char v1913; // [rsp+9AFh] [rbp-AF1h]
  char v1914; // [rsp+9B0h] [rbp-AF0h]
  char v1915; // [rsp+9B1h] [rbp-AEFh]
  char v1916; // [rsp+9C0h] [rbp-AE0h] BYREF
  char v1917; // [rsp+9C2h] [rbp-ADEh]
  char v1918; // [rsp+9C3h] [rbp-ADDh]
  char v1919; // [rsp+9C4h] [rbp-ADCh]
  char v1920; // [rsp+9C5h] [rbp-ADBh]
  char v1921; // [rsp+9C6h] [rbp-ADAh]
  char v1922; // [rsp+9C7h] [rbp-AD9h]
  char v1923; // [rsp+9C8h] [rbp-AD8h]
  char v1924; // [rsp+9C9h] [rbp-AD7h]
  char v1925; // [rsp+9CAh] [rbp-AD6h]
  char v1926; // [rsp+9CBh] [rbp-AD5h]
  char v1927; // [rsp+9CCh] [rbp-AD4h]
  char v1928; // [rsp+9CDh] [rbp-AD3h]
  char v1929; // [rsp+9CEh] [rbp-AD2h]
  char v1930; // [rsp+9CFh] [rbp-AD1h]
  char v1931; // [rsp+9D0h] [rbp-AD0h]
  char v1932; // [rsp+9D1h] [rbp-ACFh]
  char v1933; // [rsp+9D2h] [rbp-ACEh]
  char v1934; // [rsp+9D3h] [rbp-ACDh]
  char v1935; // [rsp+9D4h] [rbp-ACCh]
  char v1936; // [rsp+9D5h] [rbp-ACBh]
  char v1937; // [rsp+9D6h] [rbp-ACAh]
  char v1938; // [rsp+9D7h] [rbp-AC9h]
  char v1939; // [rsp+9D8h] [rbp-AC8h]
  char v1940; // [rsp+9D9h] [rbp-AC7h]
  char v1941; // [rsp+9DAh] [rbp-AC6h]
  char v1942; // [rsp+9DBh] [rbp-AC5h]
  char v1943; // [rsp+9DCh] [rbp-AC4h]
  char v1944; // [rsp+9DDh] [rbp-AC3h]
  char v1945; // [rsp+9DEh] [rbp-AC2h]
  char v1946; // [rsp+9DFh] [rbp-AC1h]
  char v1947; // [rsp+9E0h] [rbp-AC0h]
  char v1948; // [rsp+9E1h] [rbp-ABFh]
  char v1949; // [rsp+9E3h] [rbp-ABDh]
  char v1950; // [rsp+9E4h] [rbp-ABCh]
  char v1951; // [rsp+9E5h] [rbp-ABBh]
  char v1952; // [rsp+9E6h] [rbp-ABAh]
  char v1953; // [rsp+9E7h] [rbp-AB9h]
  char v1954; // [rsp+9E8h] [rbp-AB8h]
  char v1955; // [rsp+9E9h] [rbp-AB7h]
  char v1956; // [rsp+9EAh] [rbp-AB6h]
  char v1957; // [rsp+9EBh] [rbp-AB5h]
  char v1958; // [rsp+9ECh] [rbp-AB4h]
  char v1959; // [rsp+9EDh] [rbp-AB3h]
  char v1960; // [rsp+9EEh] [rbp-AB2h]
  char v1961; // [rsp+9EFh] [rbp-AB1h]
  char v1962; // [rsp+9F0h] [rbp-AB0h]
  char v1963; // [rsp+9F1h] [rbp-AAFh]
  char v1964; // [rsp+A00h] [rbp-AA0h] BYREF
  char v1965; // [rsp+A01h] [rbp-A9Fh]
  char v1966; // [rsp+A02h] [rbp-A9Eh]
  char v1967; // [rsp+A03h] [rbp-A9Dh]
  char v1968; // [rsp+A04h] [rbp-A9Ch]
  char v1969; // [rsp+A05h] [rbp-A9Bh]
  char v1970; // [rsp+A06h] [rbp-A9Ah]
  char v1971; // [rsp+A07h] [rbp-A99h]
  char v1972; // [rsp+A08h] [rbp-A98h]
  char v1973; // [rsp+A09h] [rbp-A97h]
  char v1974; // [rsp+A0Ah] [rbp-A96h]
  char v1975; // [rsp+A0Bh] [rbp-A95h]
  char v1976; // [rsp+A0Ch] [rbp-A94h]
  char v1977; // [rsp+A0Dh] [rbp-A93h]
  char v1978; // [rsp+A0Eh] [rbp-A92h]
  char v1979; // [rsp+A0Fh] [rbp-A91h]
  char v1980; // [rsp+A10h] [rbp-A90h]
  char v1981; // [rsp+A11h] [rbp-A8Fh]
  char v1982; // [rsp+A12h] [rbp-A8Eh]
  char v1983; // [rsp+A13h] [rbp-A8Dh]
  char v1984; // [rsp+A14h] [rbp-A8Ch]
  char v1985; // [rsp+A15h] [rbp-A8Bh]
  char v1986; // [rsp+A16h] [rbp-A8Ah]
  char v1987; // [rsp+A17h] [rbp-A89h]
  char v1988; // [rsp+A18h] [rbp-A88h]
  char v1989; // [rsp+A19h] [rbp-A87h]
  char v1990; // [rsp+A1Ah] [rbp-A86h]
  char v1991; // [rsp+A1Bh] [rbp-A85h]
  char v1992; // [rsp+A1Ch] [rbp-A84h]
  char v1993; // [rsp+A1Dh] [rbp-A83h]
  char v1994; // [rsp+A1Eh] [rbp-A82h]
  char v1995; // [rsp+A1Fh] [rbp-A81h]
  char v1996; // [rsp+A20h] [rbp-A80h]
  char v1997; // [rsp+A21h] [rbp-A7Fh]
  char v1998; // [rsp+A22h] [rbp-A7Eh]
  char v1999; // [rsp+A23h] [rbp-A7Dh]
  char v2000; // [rsp+A24h] [rbp-A7Ch]
  char v2001; // [rsp+A25h] [rbp-A7Bh]
  char v2002; // [rsp+A26h] [rbp-A7Ah]
  char v2003; // [rsp+A27h] [rbp-A79h]
  char v2004; // [rsp+A28h] [rbp-A78h]
  char v2005; // [rsp+A29h] [rbp-A77h]
  char v2006; // [rsp+A2Ah] [rbp-A76h]
  char v2007; // [rsp+A2Bh] [rbp-A75h]
  char v2008; // [rsp+A2Ch] [rbp-A74h]
  char v2009; // [rsp+A2Dh] [rbp-A73h]
  char v2010; // [rsp+A2Eh] [rbp-A72h]
  char v2011; // [rsp+A2Fh] [rbp-A71h]
  char v2012; // [rsp+A30h] [rbp-A70h]
  char v2013; // [rsp+A31h] [rbp-A6Fh]
  char v2014; // [rsp+A32h] [rbp-A6Eh]
  char v2015; // [rsp+A40h] [rbp-A60h] BYREF
  char v2016; // [rsp+A41h] [rbp-A5Fh]
  char v2017; // [rsp+A42h] [rbp-A5Eh]
  char v2018; // [rsp+A43h] [rbp-A5Dh]
  char v2019; // [rsp+A44h] [rbp-A5Ch]
  char v2020; // [rsp+A45h] [rbp-A5Bh]
  char v2021; // [rsp+A46h] [rbp-A5Ah]
  char v2022; // [rsp+A47h] [rbp-A59h]
  char v2023; // [rsp+A48h] [rbp-A58h]
  char v2024; // [rsp+A49h] [rbp-A57h]
  char v2025; // [rsp+A4Ah] [rbp-A56h]
  char v2026; // [rsp+A4Bh] [rbp-A55h]
  char v2027; // [rsp+A4Ch] [rbp-A54h]
  char v2028; // [rsp+A4Dh] [rbp-A53h]
  char v2029; // [rsp+A4Eh] [rbp-A52h]
  char v2030; // [rsp+A4Fh] [rbp-A51h]
  char v2031; // [rsp+A50h] [rbp-A50h]
  char v2032; // [rsp+A51h] [rbp-A4Fh]
  char v2033; // [rsp+A52h] [rbp-A4Eh]
  char v2034; // [rsp+A53h] [rbp-A4Dh]
  char v2035; // [rsp+A54h] [rbp-A4Ch]
  char v2036; // [rsp+A55h] [rbp-A4Bh]
  char v2037; // [rsp+A56h] [rbp-A4Ah]
  char v2038; // [rsp+A57h] [rbp-A49h]
  char v2039; // [rsp+A58h] [rbp-A48h]
  char v2040; // [rsp+A59h] [rbp-A47h]
  char v2041; // [rsp+A5Ah] [rbp-A46h]
  char v2042; // [rsp+A5Bh] [rbp-A45h]
  char v2043; // [rsp+A5Ch] [rbp-A44h]
  char v2044; // [rsp+A5Dh] [rbp-A43h]
  char v2045; // [rsp+A5Eh] [rbp-A42h]
  char v2046; // [rsp+A60h] [rbp-A40h]
  char v2047; // [rsp+A61h] [rbp-A3Fh]
  char v2048; // [rsp+A62h] [rbp-A3Eh]
  char v2049; // [rsp+A63h] [rbp-A3Dh]
  char v2050; // [rsp+A64h] [rbp-A3Ch]
  char v2051; // [rsp+A65h] [rbp-A3Bh]
  char v2052; // [rsp+A66h] [rbp-A3Ah]
  char v2053; // [rsp+A67h] [rbp-A39h]
  char v2054; // [rsp+A68h] [rbp-A38h]
  char v2055; // [rsp+A69h] [rbp-A37h]
  char v2056; // [rsp+A6Ah] [rbp-A36h]
  char v2057; // [rsp+A6Bh] [rbp-A35h]
  char v2058; // [rsp+A6Ch] [rbp-A34h]
  char v2059; // [rsp+A6Dh] [rbp-A33h]
  char v2060; // [rsp+A6Eh] [rbp-A32h]
  char v2061; // [rsp+A6Fh] [rbp-A31h]
  char v2062; // [rsp+A70h] [rbp-A30h]
  char v2063; // [rsp+A71h] [rbp-A2Fh]
  char v2064; // [rsp+A72h] [rbp-A2Eh]
  char v2065; // [rsp+A73h] [rbp-A2Dh]
  char v2066; // [rsp+A80h] [rbp-A20h] BYREF
  char v2067; // [rsp+A81h] [rbp-A1Fh]
  char v2068; // [rsp+A82h] [rbp-A1Eh]
  char v2069; // [rsp+A83h] [rbp-A1Dh]
  char v2070; // [rsp+A84h] [rbp-A1Ch]
  char v2071; // [rsp+A85h] [rbp-A1Bh]
  char v2072; // [rsp+A86h] [rbp-A1Ah]
  char v2073; // [rsp+A87h] [rbp-A19h]
  char v2074; // [rsp+A88h] [rbp-A18h]
  char v2075; // [rsp+A89h] [rbp-A17h]
  char v2076; // [rsp+A8Ah] [rbp-A16h]
  char v2077; // [rsp+A8Bh] [rbp-A15h]
  char v2078; // [rsp+A8Ch] [rbp-A14h]
  char v2079; // [rsp+A8Dh] [rbp-A13h]
  char v2080; // [rsp+A8Eh] [rbp-A12h]
  char v2081; // [rsp+A8Fh] [rbp-A11h]
  char v2082; // [rsp+A90h] [rbp-A10h]
  char v2083; // [rsp+A91h] [rbp-A0Fh]
  char v2084; // [rsp+A92h] [rbp-A0Eh]
  char v2085; // [rsp+A93h] [rbp-A0Dh]
  char v2086; // [rsp+A94h] [rbp-A0Ch]
  char v2087; // [rsp+A95h] [rbp-A0Bh]
  char v2088; // [rsp+A96h] [rbp-A0Ah]
  char v2089; // [rsp+A97h] [rbp-A09h]
  char v2090; // [rsp+A98h] [rbp-A08h]
  char v2091; // [rsp+A99h] [rbp-A07h]
  char v2092; // [rsp+A9Ah] [rbp-A06h]
  char v2093; // [rsp+A9Bh] [rbp-A05h]
  char v2094; // [rsp+A9Ch] [rbp-A04h]
  char v2095; // [rsp+A9Dh] [rbp-A03h]
  char v2096; // [rsp+A9Eh] [rbp-A02h]
  char v2097; // [rsp+A9Fh] [rbp-A01h]
  char v2098; // [rsp+AA0h] [rbp-A00h]
  char v2099; // [rsp+AA1h] [rbp-9FFh]
  char v2100; // [rsp+AA2h] [rbp-9FEh]
  char v2101; // [rsp+AA3h] [rbp-9FDh]
  char v2102; // [rsp+AA4h] [rbp-9FCh]
  char v2103; // [rsp+AA5h] [rbp-9FBh]
  char v2104; // [rsp+AA6h] [rbp-9FAh]
  char v2105; // [rsp+AA7h] [rbp-9F9h]
  char v2106; // [rsp+AA8h] [rbp-9F8h]
  char v2107; // [rsp+AA9h] [rbp-9F7h]
  char v2108; // [rsp+AAAh] [rbp-9F6h]
  char v2109; // [rsp+AABh] [rbp-9F5h]
  char v2110; // [rsp+AACh] [rbp-9F4h]
  char v2111; // [rsp+AADh] [rbp-9F3h]
  char v2112; // [rsp+AAEh] [rbp-9F2h]
  char v2113; // [rsp+AAFh] [rbp-9F1h]
  char v2114; // [rsp+AB0h] [rbp-9F0h]
  char v2115; // [rsp+AB1h] [rbp-9EFh]
  char v2116; // [rsp+AB2h] [rbp-9EEh]
  char v2117; // [rsp+AB3h] [rbp-9EDh]
  char v2118; // [rsp+AC0h] [rbp-9E0h] BYREF
  char v2119; // [rsp+AC1h] [rbp-9DFh]
  char v2120; // [rsp+AC2h] [rbp-9DEh]
  char v2121; // [rsp+AC3h] [rbp-9DDh]
  char v2122; // [rsp+AC4h] [rbp-9DCh]
  char v2123; // [rsp+AC5h] [rbp-9DBh]
  char v2124; // [rsp+AC6h] [rbp-9DAh]
  char v2125; // [rsp+AC7h] [rbp-9D9h]
  char v2126; // [rsp+AC8h] [rbp-9D8h]
  char v2127; // [rsp+AC9h] [rbp-9D7h]
  char v2128; // [rsp+ACAh] [rbp-9D6h]
  char v2129; // [rsp+ACBh] [rbp-9D5h]
  char v2130; // [rsp+ACCh] [rbp-9D4h]
  char v2131; // [rsp+ACDh] [rbp-9D3h]
  char v2132; // [rsp+ACEh] [rbp-9D2h]
  char v2133; // [rsp+ACFh] [rbp-9D1h]
  char v2134; // [rsp+AD0h] [rbp-9D0h]
  char v2135; // [rsp+AD1h] [rbp-9CFh]
  char v2136; // [rsp+AD2h] [rbp-9CEh]
  char v2137; // [rsp+AD3h] [rbp-9CDh]
  char v2138; // [rsp+AD4h] [rbp-9CCh]
  char v2139; // [rsp+AD5h] [rbp-9CBh]
  char v2140; // [rsp+AD6h] [rbp-9CAh]
  char v2141; // [rsp+AD7h] [rbp-9C9h]
  char v2142; // [rsp+AD8h] [rbp-9C8h]
  char v2143; // [rsp+AD9h] [rbp-9C7h]
  char v2144; // [rsp+ADAh] [rbp-9C6h]
  char v2145; // [rsp+ADBh] [rbp-9C5h]
  char v2146; // [rsp+ADCh] [rbp-9C4h]
  char v2147; // [rsp+ADDh] [rbp-9C3h]
  char v2148; // [rsp+ADEh] [rbp-9C2h]
  char v2149; // [rsp+ADFh] [rbp-9C1h]
  char v2150; // [rsp+AE0h] [rbp-9C0h]
  char v2151; // [rsp+AE1h] [rbp-9BFh]
  char v2152; // [rsp+AE2h] [rbp-9BEh]
  char v2153; // [rsp+AE3h] [rbp-9BDh]
  char v2154; // [rsp+AE4h] [rbp-9BCh]
  char v2155; // [rsp+AE5h] [rbp-9BBh]
  char v2156; // [rsp+AE6h] [rbp-9BAh]
  char v2157; // [rsp+AE7h] [rbp-9B9h]
  char v2158; // [rsp+AE8h] [rbp-9B8h]
  char v2159; // [rsp+AE9h] [rbp-9B7h]
  char v2160; // [rsp+AEBh] [rbp-9B5h]
  char v2161; // [rsp+AECh] [rbp-9B4h]
  char v2162; // [rsp+AEDh] [rbp-9B3h]
  char v2163; // [rsp+AEEh] [rbp-9B2h]
  char v2164; // [rsp+AEFh] [rbp-9B1h]
  char v2165; // [rsp+AF0h] [rbp-9B0h]
  char v2166; // [rsp+AF1h] [rbp-9AFh]
  char v2167; // [rsp+AF2h] [rbp-9AEh]
  char v2168; // [rsp+AF3h] [rbp-9ADh]
  char v2169; // [rsp+AF4h] [rbp-9ACh]
  char v2170; // [rsp+B00h] [rbp-9A0h] BYREF
  char v2171; // [rsp+B01h] [rbp-99Fh]
  char v2172; // [rsp+B02h] [rbp-99Eh]
  char v2173; // [rsp+B03h] [rbp-99Dh]
  char v2174; // [rsp+B04h] [rbp-99Ch]
  char v2175; // [rsp+B05h] [rbp-99Bh]
  char v2176; // [rsp+B06h] [rbp-99Ah]
  char v2177; // [rsp+B07h] [rbp-999h]
  char v2178; // [rsp+B08h] [rbp-998h]
  char v2179; // [rsp+B09h] [rbp-997h]
  char v2180; // [rsp+B0Ah] [rbp-996h]
  char v2181; // [rsp+B0Bh] [rbp-995h]
  char v2182; // [rsp+B0Ch] [rbp-994h]
  char v2183; // [rsp+B0Dh] [rbp-993h]
  char v2184; // [rsp+B0Eh] [rbp-992h]
  char v2185; // [rsp+B0Fh] [rbp-991h]
  char v2186; // [rsp+B10h] [rbp-990h]
  char v2187; // [rsp+B11h] [rbp-98Fh]
  char v2188; // [rsp+B12h] [rbp-98Eh]
  char v2189; // [rsp+B13h] [rbp-98Dh]
  char v2190; // [rsp+B14h] [rbp-98Ch]
  char v2191; // [rsp+B15h] [rbp-98Bh]
  char v2192; // [rsp+B16h] [rbp-98Ah]
  char v2193; // [rsp+B17h] [rbp-989h]
  char v2194; // [rsp+B18h] [rbp-988h]
  char v2195; // [rsp+B19h] [rbp-987h]
  char v2196; // [rsp+B1Ah] [rbp-986h]
  char v2197; // [rsp+B1Bh] [rbp-985h]
  char v2198; // [rsp+B1Ch] [rbp-984h]
  char v2199; // [rsp+B1Dh] [rbp-983h]
  char v2200; // [rsp+B1Eh] [rbp-982h]
  char v2201; // [rsp+B1Fh] [rbp-981h]
  char v2202; // [rsp+B20h] [rbp-980h]
  char v2203; // [rsp+B21h] [rbp-97Fh]
  char v2204; // [rsp+B22h] [rbp-97Eh]
  char v2205; // [rsp+B23h] [rbp-97Dh]
  char v2206; // [rsp+B24h] [rbp-97Ch]
  char v2207; // [rsp+B25h] [rbp-97Bh]
  char v2208; // [rsp+B26h] [rbp-97Ah]
  char v2209; // [rsp+B27h] [rbp-979h]
  char v2210; // [rsp+B28h] [rbp-978h]
  char v2211; // [rsp+B29h] [rbp-977h]
  char v2212; // [rsp+B2Ah] [rbp-976h]
  char v2213; // [rsp+B2Bh] [rbp-975h]
  char v2214; // [rsp+B2Ch] [rbp-974h]
  char v2215; // [rsp+B2Dh] [rbp-973h]
  char v2216; // [rsp+B2Eh] [rbp-972h]
  char v2217; // [rsp+B2Fh] [rbp-971h]
  char v2218; // [rsp+B30h] [rbp-970h]
  char v2219; // [rsp+B31h] [rbp-96Fh]
  char v2220; // [rsp+B32h] [rbp-96Eh]
  char v2221; // [rsp+B33h] [rbp-96Dh]
  char v2222; // [rsp+B34h] [rbp-96Ch]
  char v2223; // [rsp+B35h] [rbp-96Bh]
  char v2224; // [rsp+B40h] [rbp-960h] BYREF
  char v2225; // [rsp+B41h] [rbp-95Fh]
  char v2226; // [rsp+B42h] [rbp-95Eh]
  char v2227; // [rsp+B43h] [rbp-95Dh]
  char v2228; // [rsp+B44h] [rbp-95Ch]
  char v2229; // [rsp+B45h] [rbp-95Bh]
  char v2230; // [rsp+B46h] [rbp-95Ah]
  char v2231; // [rsp+B47h] [rbp-959h]
  char v2232; // [rsp+B48h] [rbp-958h]
  char v2233; // [rsp+B49h] [rbp-957h]
  char v2234; // [rsp+B4Ah] [rbp-956h]
  char v2235; // [rsp+B4Bh] [rbp-955h]
  char v2236; // [rsp+B4Ch] [rbp-954h]
  char v2237; // [rsp+B4Dh] [rbp-953h]
  char v2238; // [rsp+B4Eh] [rbp-952h]
  char v2239; // [rsp+B4Fh] [rbp-951h]
  char v2240; // [rsp+B50h] [rbp-950h]
  char v2241; // [rsp+B51h] [rbp-94Fh]
  char v2242; // [rsp+B52h] [rbp-94Eh]
  char v2243; // [rsp+B53h] [rbp-94Dh]
  char v2244; // [rsp+B54h] [rbp-94Ch]
  char v2245; // [rsp+B55h] [rbp-94Bh]
  char v2246; // [rsp+B56h] [rbp-94Ah]
  char v2247; // [rsp+B57h] [rbp-949h]
  char v2248; // [rsp+B58h] [rbp-948h]
  char v2249; // [rsp+B59h] [rbp-947h]
  char v2250; // [rsp+B5Ah] [rbp-946h]
  char v2251; // [rsp+B5Bh] [rbp-945h]
  char v2252; // [rsp+B5Ch] [rbp-944h]
  char v2253; // [rsp+B5Dh] [rbp-943h]
  char v2254; // [rsp+B5Eh] [rbp-942h]
  char v2255; // [rsp+B5Fh] [rbp-941h]
  char v2256; // [rsp+B60h] [rbp-940h]
  char v2257; // [rsp+B61h] [rbp-93Fh]
  char v2258; // [rsp+B62h] [rbp-93Eh]
  char v2259; // [rsp+B63h] [rbp-93Dh]
  char v2260; // [rsp+B64h] [rbp-93Ch]
  char v2261; // [rsp+B65h] [rbp-93Bh]
  char v2262; // [rsp+B66h] [rbp-93Ah]
  char v2263; // [rsp+B67h] [rbp-939h]
  char v2264; // [rsp+B68h] [rbp-938h]
  char v2265; // [rsp+B69h] [rbp-937h]
  char v2266; // [rsp+B6Ah] [rbp-936h]
  char v2267; // [rsp+B6Bh] [rbp-935h]
  char v2268; // [rsp+B6Ch] [rbp-934h]
  char v2269; // [rsp+B6Dh] [rbp-933h]
  char v2270; // [rsp+B6Eh] [rbp-932h]
  char v2271; // [rsp+B6Fh] [rbp-931h]
  char v2272; // [rsp+B70h] [rbp-930h]
  char v2273; // [rsp+B71h] [rbp-92Fh]
  char v2274; // [rsp+B72h] [rbp-92Eh]
  char v2275; // [rsp+B73h] [rbp-92Dh]
  char v2276; // [rsp+B74h] [rbp-92Ch]
  char v2277; // [rsp+B75h] [rbp-92Bh]
  char v2278; // [rsp+B76h] [rbp-92Ah]
  char v2279; // [rsp+B80h] [rbp-920h] BYREF
  char v2280; // [rsp+B81h] [rbp-91Fh]
  char v2281; // [rsp+B82h] [rbp-91Eh]
  char v2282; // [rsp+B83h] [rbp-91Dh]
  char v2283; // [rsp+B84h] [rbp-91Ch]
  char v2284; // [rsp+B85h] [rbp-91Bh]
  char v2285; // [rsp+B86h] [rbp-91Ah]
  char v2286; // [rsp+B87h] [rbp-919h]
  char v2287; // [rsp+B88h] [rbp-918h]
  char v2288; // [rsp+B89h] [rbp-917h]
  char v2289; // [rsp+B8Ah] [rbp-916h]
  char v2290; // [rsp+B8Bh] [rbp-915h]
  char v2291; // [rsp+B8Ch] [rbp-914h]
  char v2292; // [rsp+B8Dh] [rbp-913h]
  char v2293; // [rsp+B8Eh] [rbp-912h]
  char v2294; // [rsp+B8Fh] [rbp-911h]
  char v2295; // [rsp+B90h] [rbp-910h]
  char v2296; // [rsp+B91h] [rbp-90Fh]
  char v2297; // [rsp+B92h] [rbp-90Eh]
  char v2298; // [rsp+B93h] [rbp-90Dh]
  char v2299; // [rsp+B94h] [rbp-90Ch]
  char v2300; // [rsp+B95h] [rbp-90Bh]
  char v2301; // [rsp+B96h] [rbp-90Ah]
  char v2302; // [rsp+B97h] [rbp-909h]
  char v2303; // [rsp+B98h] [rbp-908h]
  char v2304; // [rsp+B99h] [rbp-907h]
  char v2305; // [rsp+B9Ah] [rbp-906h]
  char v2306; // [rsp+B9Bh] [rbp-905h]
  char v2307; // [rsp+B9Ch] [rbp-904h]
  char v2308; // [rsp+B9Dh] [rbp-903h]
  char v2309; // [rsp+B9Eh] [rbp-902h]
  char v2310; // [rsp+B9Fh] [rbp-901h]
  char v2311; // [rsp+BA0h] [rbp-900h]
  char v2312; // [rsp+BA1h] [rbp-8FFh]
  char v2313; // [rsp+BA2h] [rbp-8FEh]
  char v2314; // [rsp+BA3h] [rbp-8FDh]
  char v2315; // [rsp+BA4h] [rbp-8FCh]
  char v2316; // [rsp+BA5h] [rbp-8FBh]
  char v2317; // [rsp+BA6h] [rbp-8FAh]
  char v2318; // [rsp+BA7h] [rbp-8F9h]
  char v2319; // [rsp+BA8h] [rbp-8F8h]
  char v2320; // [rsp+BA9h] [rbp-8F7h]
  char v2321; // [rsp+BAAh] [rbp-8F6h]
  char v2322; // [rsp+BABh] [rbp-8F5h]
  char v2323; // [rsp+BACh] [rbp-8F4h]
  char v2324; // [rsp+BADh] [rbp-8F3h]
  char v2325; // [rsp+BAEh] [rbp-8F2h]
  char v2326; // [rsp+BAFh] [rbp-8F1h]
  char v2327; // [rsp+BB0h] [rbp-8F0h]
  char v2328; // [rsp+BB1h] [rbp-8EFh]
  char v2329; // [rsp+BB2h] [rbp-8EEh]
  char v2330; // [rsp+BB3h] [rbp-8EDh]
  char v2331; // [rsp+BB4h] [rbp-8ECh]
  char v2332; // [rsp+BB5h] [rbp-8EBh]
  char v2333; // [rsp+BB6h] [rbp-8EAh]
  char v2334; // [rsp+BB7h] [rbp-8E9h]
  char v2335; // [rsp+BC0h] [rbp-8E0h] BYREF
  char v2336; // [rsp+BC1h] [rbp-8DFh]
  char v2337; // [rsp+BC2h] [rbp-8DEh]
  char v2338; // [rsp+BC3h] [rbp-8DDh]
  char v2339; // [rsp+BC4h] [rbp-8DCh]
  char v2340; // [rsp+BC5h] [rbp-8DBh]
  char v2341; // [rsp+BC6h] [rbp-8DAh]
  char v2342; // [rsp+BC7h] [rbp-8D9h]
  char v2343; // [rsp+BC8h] [rbp-8D8h]
  char v2344; // [rsp+BC9h] [rbp-8D7h]
  char v2345; // [rsp+BCAh] [rbp-8D6h]
  char v2346; // [rsp+BCBh] [rbp-8D5h]
  char v2347; // [rsp+BCCh] [rbp-8D4h]
  char v2348; // [rsp+BCDh] [rbp-8D3h]
  char v2349; // [rsp+BCEh] [rbp-8D2h]
  char v2350; // [rsp+BCFh] [rbp-8D1h]
  char v2351; // [rsp+BD0h] [rbp-8D0h]
  char v2352; // [rsp+BD1h] [rbp-8CFh]
  char v2353; // [rsp+BD2h] [rbp-8CEh]
  char v2354; // [rsp+BD3h] [rbp-8CDh]
  char v2355; // [rsp+BD4h] [rbp-8CCh]
  char v2356; // [rsp+BD5h] [rbp-8CBh]
  char v2357; // [rsp+BD6h] [rbp-8CAh]
  char v2358; // [rsp+BD7h] [rbp-8C9h]
  char v2359; // [rsp+BD8h] [rbp-8C8h]
  char v2360; // [rsp+BD9h] [rbp-8C7h]
  char v2361; // [rsp+BDAh] [rbp-8C6h]
  char v2362; // [rsp+BDBh] [rbp-8C5h]
  char v2363; // [rsp+BDCh] [rbp-8C4h]
  char v2364; // [rsp+BDDh] [rbp-8C3h]
  char v2365; // [rsp+BDEh] [rbp-8C2h]
  char v2366; // [rsp+BDFh] [rbp-8C1h]
  char v2367; // [rsp+BE0h] [rbp-8C0h]
  char v2368; // [rsp+BE1h] [rbp-8BFh]
  char v2369; // [rsp+BE2h] [rbp-8BEh]
  char v2370; // [rsp+BE3h] [rbp-8BDh]
  char v2371; // [rsp+BE4h] [rbp-8BCh]
  char v2372; // [rsp+BE5h] [rbp-8BBh]
  char v2373; // [rsp+BE6h] [rbp-8BAh]
  char v2374; // [rsp+BE7h] [rbp-8B9h]
  char v2375; // [rsp+BE8h] [rbp-8B8h]
  char v2376; // [rsp+BE9h] [rbp-8B7h]
  char v2377; // [rsp+BEAh] [rbp-8B6h]
  char v2378; // [rsp+BEBh] [rbp-8B5h]
  char v2379; // [rsp+BECh] [rbp-8B4h]
  char v2380; // [rsp+BEDh] [rbp-8B3h]
  char v2381; // [rsp+BEEh] [rbp-8B2h]
  char v2382; // [rsp+BEFh] [rbp-8B1h]
  char v2383; // [rsp+BF0h] [rbp-8B0h]
  char v2384; // [rsp+BF1h] [rbp-8AFh]
  char v2385; // [rsp+BF2h] [rbp-8AEh]
  char v2386; // [rsp+BF3h] [rbp-8ADh]
  char v2387; // [rsp+BF4h] [rbp-8ACh]
  char v2388; // [rsp+BF5h] [rbp-8ABh]
  char v2389; // [rsp+BF6h] [rbp-8AAh]
  char v2390; // [rsp+BF7h] [rbp-8A9h]
  char v2391; // [rsp+C00h] [rbp-8A0h] BYREF
  char v2392; // [rsp+C01h] [rbp-89Fh]
  char v2393; // [rsp+C02h] [rbp-89Eh]
  char v2394; // [rsp+C03h] [rbp-89Dh]
  char v2395; // [rsp+C04h] [rbp-89Ch]
  char v2396; // [rsp+C05h] [rbp-89Bh]
  char v2397; // [rsp+C06h] [rbp-89Ah]
  char v2398; // [rsp+C07h] [rbp-899h]
  char v2399; // [rsp+C08h] [rbp-898h]
  char v2400; // [rsp+C09h] [rbp-897h]
  char v2401; // [rsp+C0Ah] [rbp-896h]
  char v2402; // [rsp+C0Bh] [rbp-895h]
  char v2403; // [rsp+C0Ch] [rbp-894h]
  char v2404; // [rsp+C0Dh] [rbp-893h]
  char v2405; // [rsp+C0Eh] [rbp-892h]
  char v2406; // [rsp+C0Fh] [rbp-891h]
  char v2407; // [rsp+C10h] [rbp-890h]
  char v2408; // [rsp+C11h] [rbp-88Fh]
  char v2409; // [rsp+C12h] [rbp-88Eh]
  char v2410; // [rsp+C13h] [rbp-88Dh]
  char v2411; // [rsp+C14h] [rbp-88Ch]
  char v2412; // [rsp+C15h] [rbp-88Bh]
  char v2413; // [rsp+C16h] [rbp-88Ah]
  char v2414; // [rsp+C17h] [rbp-889h]
  char v2415; // [rsp+C18h] [rbp-888h]
  char v2416; // [rsp+C19h] [rbp-887h]
  char v2417; // [rsp+C1Ah] [rbp-886h]
  char v2418; // [rsp+C1Bh] [rbp-885h]
  char v2419; // [rsp+C1Ch] [rbp-884h]
  char v2420; // [rsp+C1Dh] [rbp-883h]
  char v2421; // [rsp+C1Eh] [rbp-882h]
  char v2422; // [rsp+C1Fh] [rbp-881h]
  char v2423; // [rsp+C20h] [rbp-880h]
  char v2424; // [rsp+C21h] [rbp-87Fh]
  char v2425; // [rsp+C22h] [rbp-87Eh]
  char v2426; // [rsp+C23h] [rbp-87Dh]
  char v2427; // [rsp+C24h] [rbp-87Ch]
  char v2428; // [rsp+C25h] [rbp-87Bh]
  char v2429; // [rsp+C26h] [rbp-87Ah]
  char v2430; // [rsp+C27h] [rbp-879h]
  char v2431; // [rsp+C28h] [rbp-878h]
  char v2432; // [rsp+C29h] [rbp-877h]
  char v2433; // [rsp+C2Ah] [rbp-876h]
  char v2434; // [rsp+C2Bh] [rbp-875h]
  char v2435; // [rsp+C2Ch] [rbp-874h]
  char v2436; // [rsp+C2Dh] [rbp-873h]
  char v2437; // [rsp+C2Eh] [rbp-872h]
  char v2438; // [rsp+C2Fh] [rbp-871h]
  char v2439; // [rsp+C30h] [rbp-870h]
  char v2440; // [rsp+C31h] [rbp-86Fh]
  char v2441; // [rsp+C32h] [rbp-86Eh]
  char v2442; // [rsp+C33h] [rbp-86Dh]
  char v2443; // [rsp+C34h] [rbp-86Ch]
  char v2444; // [rsp+C35h] [rbp-86Bh]
  char v2445; // [rsp+C36h] [rbp-86Ah]
  char v2446; // [rsp+C37h] [rbp-869h]
  char v2447; // [rsp+C38h] [rbp-868h]
  char v2448; // [rsp+C40h] [rbp-860h] BYREF
  char v2449; // [rsp+C41h] [rbp-85Fh]
  char v2450; // [rsp+C42h] [rbp-85Eh]
  char v2451; // [rsp+C43h] [rbp-85Dh]
  char v2452; // [rsp+C44h] [rbp-85Ch]
  char v2453; // [rsp+C45h] [rbp-85Bh]
  char v2454; // [rsp+C46h] [rbp-85Ah]
  char v2455; // [rsp+C47h] [rbp-859h]
  char v2456; // [rsp+C48h] [rbp-858h]
  char v2457; // [rsp+C49h] [rbp-857h]
  char v2458; // [rsp+C4Ah] [rbp-856h]
  char v2459; // [rsp+C4Bh] [rbp-855h]
  char v2460; // [rsp+C4Ch] [rbp-854h]
  char v2461; // [rsp+C4Dh] [rbp-853h]
  char v2462; // [rsp+C4Eh] [rbp-852h]
  char v2463; // [rsp+C4Fh] [rbp-851h]
  char v2464; // [rsp+C50h] [rbp-850h]
  char v2465; // [rsp+C51h] [rbp-84Fh]
  char v2466; // [rsp+C52h] [rbp-84Eh]
  char v2467; // [rsp+C53h] [rbp-84Dh]
  char v2468; // [rsp+C54h] [rbp-84Ch]
  char v2469; // [rsp+C55h] [rbp-84Bh]
  char v2470; // [rsp+C56h] [rbp-84Ah]
  char v2471; // [rsp+C57h] [rbp-849h]
  char v2472; // [rsp+C58h] [rbp-848h]
  char v2473; // [rsp+C59h] [rbp-847h]
  char v2474; // [rsp+C5Ah] [rbp-846h]
  char v2475; // [rsp+C5Bh] [rbp-845h]
  char v2476; // [rsp+C5Ch] [rbp-844h]
  char v2477; // [rsp+C5Dh] [rbp-843h]
  char v2478; // [rsp+C5Eh] [rbp-842h]
  char v2479; // [rsp+C5Fh] [rbp-841h]
  char v2480; // [rsp+C60h] [rbp-840h]
  char v2481; // [rsp+C61h] [rbp-83Fh]
  char v2482; // [rsp+C62h] [rbp-83Eh]
  char v2483; // [rsp+C63h] [rbp-83Dh]
  char v2484; // [rsp+C64h] [rbp-83Ch]
  char v2485; // [rsp+C65h] [rbp-83Bh]
  char v2486; // [rsp+C66h] [rbp-83Ah]
  char v2487; // [rsp+C67h] [rbp-839h]
  char v2488; // [rsp+C68h] [rbp-838h]
  char v2489; // [rsp+C69h] [rbp-837h]
  char v2490; // [rsp+C6Ah] [rbp-836h]
  char v2491; // [rsp+C6Bh] [rbp-835h]
  char v2492; // [rsp+C6Ch] [rbp-834h]
  char v2493; // [rsp+C6Dh] [rbp-833h]
  char v2494; // [rsp+C6Eh] [rbp-832h]
  char v2495; // [rsp+C6Fh] [rbp-831h]
  char v2496; // [rsp+C70h] [rbp-830h]
  char v2497; // [rsp+C71h] [rbp-82Fh]
  char v2498; // [rsp+C72h] [rbp-82Eh]
  char v2499; // [rsp+C73h] [rbp-82Dh]
  char v2500; // [rsp+C74h] [rbp-82Ch]
  char v2501; // [rsp+C75h] [rbp-82Bh]
  char v2502; // [rsp+C76h] [rbp-82Ah]
  char v2503; // [rsp+C77h] [rbp-829h]
  char v2504; // [rsp+C78h] [rbp-828h]
  char v2505; // [rsp+C79h] [rbp-827h]
  char v2506; // [rsp+C80h] [rbp-820h] BYREF
  char v2507; // [rsp+C81h] [rbp-81Fh]
  char v2508; // [rsp+C82h] [rbp-81Eh]
  char v2509; // [rsp+C83h] [rbp-81Dh]
  char v2510; // [rsp+C84h] [rbp-81Ch]
  char v2511; // [rsp+C85h] [rbp-81Bh]
  char v2512; // [rsp+C86h] [rbp-81Ah]
  char v2513; // [rsp+C87h] [rbp-819h]
  char v2514; // [rsp+C88h] [rbp-818h]
  char v2515; // [rsp+C89h] [rbp-817h]
  char v2516; // [rsp+C8Ah] [rbp-816h]
  char v2517; // [rsp+C8Bh] [rbp-815h]
  char v2518; // [rsp+C8Ch] [rbp-814h]
  char v2519; // [rsp+C8Dh] [rbp-813h]
  char v2520; // [rsp+C8Eh] [rbp-812h]
  char v2521; // [rsp+C8Fh] [rbp-811h]
  char v2522; // [rsp+C90h] [rbp-810h]
  char v2523; // [rsp+C91h] [rbp-80Fh]
  char v2524; // [rsp+C92h] [rbp-80Eh]
  char v2525; // [rsp+C93h] [rbp-80Dh]
  char v2526; // [rsp+C94h] [rbp-80Ch]
  char v2527; // [rsp+C95h] [rbp-80Bh]
  char v2528; // [rsp+C96h] [rbp-80Ah]
  char v2529; // [rsp+C97h] [rbp-809h]
  char v2530; // [rsp+C98h] [rbp-808h]
  char v2531; // [rsp+C99h] [rbp-807h]
  char v2532; // [rsp+C9Ah] [rbp-806h]
  char v2533; // [rsp+C9Bh] [rbp-805h]
  char v2534; // [rsp+C9Ch] [rbp-804h]
  char v2535; // [rsp+C9Dh] [rbp-803h]
  char v2536; // [rsp+C9Eh] [rbp-802h]
  char v2537; // [rsp+C9Fh] [rbp-801h]
  char v2538; // [rsp+CA0h] [rbp-800h]
  char v2539; // [rsp+CA1h] [rbp-7FFh]
  char v2540; // [rsp+CA2h] [rbp-7FEh]
  char v2541; // [rsp+CA3h] [rbp-7FDh]
  char v2542; // [rsp+CA4h] [rbp-7FCh]
  char v2543; // [rsp+CA5h] [rbp-7FBh]
  char v2544; // [rsp+CA6h] [rbp-7FAh]
  char v2545; // [rsp+CA7h] [rbp-7F9h]
  char v2546; // [rsp+CA8h] [rbp-7F8h]
  char v2547; // [rsp+CA9h] [rbp-7F7h]
  char v2548; // [rsp+CAAh] [rbp-7F6h]
  char v2549; // [rsp+CABh] [rbp-7F5h]
  char v2550; // [rsp+CACh] [rbp-7F4h]
  char v2551; // [rsp+CADh] [rbp-7F3h]
  char v2552; // [rsp+CAEh] [rbp-7F2h]
  char v2553; // [rsp+CAFh] [rbp-7F1h]
  char v2554; // [rsp+CB0h] [rbp-7F0h]
  char v2555; // [rsp+CB1h] [rbp-7EFh]
  char v2556; // [rsp+CB2h] [rbp-7EEh]
  char v2557; // [rsp+CB3h] [rbp-7EDh]
  char v2558; // [rsp+CB4h] [rbp-7ECh]
  char v2559; // [rsp+CB5h] [rbp-7EBh]
  char v2560; // [rsp+CB6h] [rbp-7EAh]
  char v2561; // [rsp+CB7h] [rbp-7E9h]
  char v2562; // [rsp+CB8h] [rbp-7E8h]
  char v2563; // [rsp+CB9h] [rbp-7E7h]
  char v2564; // [rsp+CC0h] [rbp-7E0h] BYREF
  char v2565; // [rsp+CC1h] [rbp-7DFh]
  char v2566; // [rsp+CC2h] [rbp-7DEh]
  char v2567; // [rsp+CC3h] [rbp-7DDh]
  char v2568; // [rsp+CC4h] [rbp-7DCh]
  char v2569; // [rsp+CC5h] [rbp-7DBh]
  char v2570; // [rsp+CC6h] [rbp-7DAh]
  char v2571; // [rsp+CC7h] [rbp-7D9h]
  char v2572; // [rsp+CC8h] [rbp-7D8h]
  char v2573; // [rsp+CC9h] [rbp-7D7h]
  char v2574; // [rsp+CCAh] [rbp-7D6h]
  char v2575; // [rsp+CCBh] [rbp-7D5h]
  char v2576; // [rsp+CCCh] [rbp-7D4h]
  char v2577; // [rsp+CCDh] [rbp-7D3h]
  char v2578; // [rsp+CCEh] [rbp-7D2h]
  char v2579; // [rsp+CCFh] [rbp-7D1h]
  char v2580; // [rsp+CD0h] [rbp-7D0h]
  char v2581; // [rsp+CD1h] [rbp-7CFh]
  char v2582; // [rsp+CD2h] [rbp-7CEh]
  char v2583; // [rsp+CD3h] [rbp-7CDh]
  char v2584; // [rsp+CD4h] [rbp-7CCh]
  char v2585; // [rsp+CD5h] [rbp-7CBh]
  char v2586; // [rsp+CD6h] [rbp-7CAh]
  char v2587; // [rsp+CD7h] [rbp-7C9h]
  char v2588; // [rsp+CD8h] [rbp-7C8h]
  char v2589; // [rsp+CD9h] [rbp-7C7h]
  char v2590; // [rsp+CDAh] [rbp-7C6h]
  char v2591; // [rsp+CDBh] [rbp-7C5h]
  char v2592; // [rsp+CDCh] [rbp-7C4h]
  char v2593; // [rsp+CDDh] [rbp-7C3h]
  char v2594; // [rsp+CDEh] [rbp-7C2h]
  char v2595; // [rsp+CDFh] [rbp-7C1h]
  char v2596; // [rsp+CE0h] [rbp-7C0h]
  char v2597; // [rsp+CE1h] [rbp-7BFh]
  char v2598; // [rsp+CE2h] [rbp-7BEh]
  char v2599; // [rsp+CE3h] [rbp-7BDh]
  char v2600; // [rsp+CE4h] [rbp-7BCh]
  char v2601; // [rsp+CE5h] [rbp-7BBh]
  char v2602; // [rsp+CE6h] [rbp-7BAh]
  char v2603; // [rsp+CE7h] [rbp-7B9h]
  char v2604; // [rsp+CE8h] [rbp-7B8h]
  char v2605; // [rsp+CE9h] [rbp-7B7h]
  char v2606; // [rsp+CEAh] [rbp-7B6h]
  char v2607; // [rsp+CEBh] [rbp-7B5h]
  char v2608; // [rsp+CECh] [rbp-7B4h]
  char v2609; // [rsp+CEDh] [rbp-7B3h]
  char v2610; // [rsp+CEEh] [rbp-7B2h]
  char v2611; // [rsp+CEFh] [rbp-7B1h]
  char v2612; // [rsp+CF0h] [rbp-7B0h]
  char v2613; // [rsp+CF1h] [rbp-7AFh]
  char v2614; // [rsp+CF2h] [rbp-7AEh]
  char v2615; // [rsp+CF3h] [rbp-7ADh]
  char v2616; // [rsp+CF4h] [rbp-7ACh]
  char v2617; // [rsp+CF5h] [rbp-7ABh]
  char v2618; // [rsp+CF6h] [rbp-7AAh]
  char v2619; // [rsp+CF7h] [rbp-7A9h]
  char v2620; // [rsp+CF8h] [rbp-7A8h]
  char v2621; // [rsp+CF9h] [rbp-7A7h]
  char v2622; // [rsp+CFAh] [rbp-7A6h]
  char v2623; // [rsp+D00h] [rbp-7A0h] BYREF
  char v2624; // [rsp+D01h] [rbp-79Fh]
  char v2625; // [rsp+D02h] [rbp-79Eh]
  char v2626; // [rsp+D03h] [rbp-79Dh]
  char v2627; // [rsp+D04h] [rbp-79Ch]
  char v2628; // [rsp+D05h] [rbp-79Bh]
  char v2629; // [rsp+D06h] [rbp-79Ah]
  char v2630; // [rsp+D07h] [rbp-799h]
  char v2631; // [rsp+D08h] [rbp-798h]
  char v2632; // [rsp+D09h] [rbp-797h]
  char v2633; // [rsp+D0Ah] [rbp-796h]
  char v2634; // [rsp+D0Bh] [rbp-795h]
  char v2635; // [rsp+D0Ch] [rbp-794h]
  char v2636; // [rsp+D0Dh] [rbp-793h]
  char v2637; // [rsp+D0Eh] [rbp-792h]
  char v2638; // [rsp+D0Fh] [rbp-791h]
  char v2639; // [rsp+D10h] [rbp-790h]
  char v2640; // [rsp+D11h] [rbp-78Fh]
  char v2641; // [rsp+D12h] [rbp-78Eh]
  char v2642; // [rsp+D13h] [rbp-78Dh]
  char v2643; // [rsp+D14h] [rbp-78Ch]
  char v2644; // [rsp+D15h] [rbp-78Bh]
  char v2645; // [rsp+D16h] [rbp-78Ah]
  char v2646; // [rsp+D17h] [rbp-789h]
  char v2647; // [rsp+D18h] [rbp-788h]
  char v2648; // [rsp+D19h] [rbp-787h]
  char v2649; // [rsp+D1Ah] [rbp-786h]
  char v2650; // [rsp+D1Bh] [rbp-785h]
  char v2651; // [rsp+D1Ch] [rbp-784h]
  char v2652; // [rsp+D1Dh] [rbp-783h]
  char v2653; // [rsp+D1Eh] [rbp-782h]
  char v2654; // [rsp+D1Fh] [rbp-781h]
  char v2655; // [rsp+D20h] [rbp-780h]
  char v2656; // [rsp+D21h] [rbp-77Fh]
  char v2657; // [rsp+D22h] [rbp-77Eh]
  char v2658; // [rsp+D23h] [rbp-77Dh]
  char v2659; // [rsp+D24h] [rbp-77Ch]
  char v2660; // [rsp+D25h] [rbp-77Bh]
  char v2661; // [rsp+D26h] [rbp-77Ah]
  char v2662; // [rsp+D27h] [rbp-779h]
  char v2663; // [rsp+D28h] [rbp-778h]
  char v2664; // [rsp+D29h] [rbp-777h]
  char v2665; // [rsp+D2Ah] [rbp-776h]
  char v2666; // [rsp+D2Bh] [rbp-775h]
  char v2667; // [rsp+D2Ch] [rbp-774h]
  char v2668; // [rsp+D2Dh] [rbp-773h]
  char v2669; // [rsp+D2Eh] [rbp-772h]
  char v2670; // [rsp+D2Fh] [rbp-771h]
  char v2671; // [rsp+D30h] [rbp-770h]
  char v2672; // [rsp+D31h] [rbp-76Fh]
  char v2673; // [rsp+D32h] [rbp-76Eh]
  char v2674; // [rsp+D33h] [rbp-76Dh]
  char v2675; // [rsp+D34h] [rbp-76Ch]
  char v2676; // [rsp+D35h] [rbp-76Bh]
  char v2677; // [rsp+D36h] [rbp-76Ah]
  char v2678; // [rsp+D37h] [rbp-769h]
  char v2679; // [rsp+D38h] [rbp-768h]
  char v2680; // [rsp+D39h] [rbp-767h]
  char v2681; // [rsp+D3Ah] [rbp-766h]
  char v2682; // [rsp+D40h] [rbp-760h] BYREF
  char v2683; // [rsp+D41h] [rbp-75Fh]
  char v2684; // [rsp+D42h] [rbp-75Eh]
  char v2685; // [rsp+D43h] [rbp-75Dh]
  char v2686; // [rsp+D44h] [rbp-75Ch]
  char v2687; // [rsp+D45h] [rbp-75Bh]
  char v2688; // [rsp+D46h] [rbp-75Ah]
  char v2689; // [rsp+D47h] [rbp-759h]
  char v2690; // [rsp+D48h] [rbp-758h]
  char v2691; // [rsp+D49h] [rbp-757h]
  char v2692; // [rsp+D4Ah] [rbp-756h]
  char v2693; // [rsp+D4Bh] [rbp-755h]
  char v2694; // [rsp+D4Ch] [rbp-754h]
  char v2695; // [rsp+D4Dh] [rbp-753h]
  char v2696; // [rsp+D4Eh] [rbp-752h]
  char v2697; // [rsp+D4Fh] [rbp-751h]
  char v2698; // [rsp+D50h] [rbp-750h]
  char v2699; // [rsp+D51h] [rbp-74Fh]
  char v2700; // [rsp+D52h] [rbp-74Eh]
  char v2701; // [rsp+D53h] [rbp-74Dh]
  char v2702; // [rsp+D54h] [rbp-74Ch]
  char v2703; // [rsp+D55h] [rbp-74Bh]
  char v2704; // [rsp+D56h] [rbp-74Ah]
  char v2705; // [rsp+D57h] [rbp-749h]
  char v2706; // [rsp+D58h] [rbp-748h]
  char v2707; // [rsp+D59h] [rbp-747h]
  char v2708; // [rsp+D5Ah] [rbp-746h]
  char v2709; // [rsp+D5Bh] [rbp-745h]
  char v2710; // [rsp+D5Ch] [rbp-744h]
  char v2711; // [rsp+D5Dh] [rbp-743h]
  char v2712; // [rsp+D5Eh] [rbp-742h]
  char v2713; // [rsp+D5Fh] [rbp-741h]
  char v2714; // [rsp+D60h] [rbp-740h]
  char v2715; // [rsp+D61h] [rbp-73Fh]
  char v2716; // [rsp+D62h] [rbp-73Eh]
  char v2717; // [rsp+D63h] [rbp-73Dh]
  char v2718; // [rsp+D64h] [rbp-73Ch]
  char v2719; // [rsp+D65h] [rbp-73Bh]
  char v2720; // [rsp+D66h] [rbp-73Ah]
  char v2721; // [rsp+D67h] [rbp-739h]
  char v2722; // [rsp+D68h] [rbp-738h]
  char v2723; // [rsp+D69h] [rbp-737h]
  char v2724; // [rsp+D6Ah] [rbp-736h]
  char v2725; // [rsp+D6Bh] [rbp-735h]
  char v2726; // [rsp+D6Ch] [rbp-734h]
  char v2727; // [rsp+D6Dh] [rbp-733h]
  char v2728; // [rsp+D6Eh] [rbp-732h]
  char v2729; // [rsp+D6Fh] [rbp-731h]
  char v2730; // [rsp+D70h] [rbp-730h]
  char v2731; // [rsp+D71h] [rbp-72Fh]
  char v2732; // [rsp+D72h] [rbp-72Eh]
  char v2733; // [rsp+D73h] [rbp-72Dh]
  char v2734; // [rsp+D74h] [rbp-72Ch]
  char v2735; // [rsp+D75h] [rbp-72Bh]
  char v2736; // [rsp+D76h] [rbp-72Ah]
  char v2737; // [rsp+D77h] [rbp-729h]
  char v2738; // [rsp+D78h] [rbp-728h]
  char v2739; // [rsp+D79h] [rbp-727h]
  char v2740; // [rsp+D7Ah] [rbp-726h]
  char v2741; // [rsp+D80h] [rbp-720h] BYREF
  char v2742; // [rsp+D81h] [rbp-71Fh]
  char v2743; // [rsp+D82h] [rbp-71Eh]
  char v2744; // [rsp+D83h] [rbp-71Dh]
  char v2745; // [rsp+D84h] [rbp-71Ch]
  char v2746; // [rsp+D85h] [rbp-71Bh]
  char v2747; // [rsp+D86h] [rbp-71Ah]
  char v2748; // [rsp+D87h] [rbp-719h]
  char v2749; // [rsp+D88h] [rbp-718h]
  char v2750; // [rsp+D89h] [rbp-717h]
  char v2751; // [rsp+D8Ah] [rbp-716h]
  char v2752; // [rsp+D8Bh] [rbp-715h]
  char v2753; // [rsp+D8Ch] [rbp-714h]
  char v2754; // [rsp+D8Dh] [rbp-713h]
  char v2755; // [rsp+D8Eh] [rbp-712h]
  char v2756; // [rsp+D8Fh] [rbp-711h]
  char v2757; // [rsp+D90h] [rbp-710h]
  char v2758; // [rsp+D91h] [rbp-70Fh]
  char v2759; // [rsp+D92h] [rbp-70Eh]
  char v2760; // [rsp+D93h] [rbp-70Dh]
  char v2761; // [rsp+D94h] [rbp-70Ch]
  char v2762; // [rsp+D95h] [rbp-70Bh]
  char v2763; // [rsp+D96h] [rbp-70Ah]
  char v2764; // [rsp+D97h] [rbp-709h]
  char v2765; // [rsp+D98h] [rbp-708h]
  char v2766; // [rsp+D99h] [rbp-707h]
  char v2767; // [rsp+D9Ah] [rbp-706h]
  char v2768; // [rsp+D9Bh] [rbp-705h]
  char v2769; // [rsp+D9Dh] [rbp-703h]
  char v2770; // [rsp+D9Eh] [rbp-702h]
  char v2771; // [rsp+D9Fh] [rbp-701h]
  char v2772; // [rsp+DA0h] [rbp-700h]
  char v2773; // [rsp+DA1h] [rbp-6FFh]
  char v2774; // [rsp+DA2h] [rbp-6FEh]
  char v2775; // [rsp+DA3h] [rbp-6FDh]
  char v2776; // [rsp+DA4h] [rbp-6FCh]
  char v2777; // [rsp+DA5h] [rbp-6FBh]
  char v2778; // [rsp+DA6h] [rbp-6FAh]
  char v2779; // [rsp+DA7h] [rbp-6F9h]
  char v2780; // [rsp+DA8h] [rbp-6F8h]
  char v2781; // [rsp+DA9h] [rbp-6F7h]
  char v2782; // [rsp+DAAh] [rbp-6F6h]
  char v2783; // [rsp+DABh] [rbp-6F5h]
  char v2784; // [rsp+DACh] [rbp-6F4h]
  char v2785; // [rsp+DADh] [rbp-6F3h]
  char v2786; // [rsp+DAEh] [rbp-6F2h]
  char v2787; // [rsp+DAFh] [rbp-6F1h]
  char v2788; // [rsp+DB0h] [rbp-6F0h]
  char v2789; // [rsp+DB1h] [rbp-6EFh]
  char v2790; // [rsp+DB2h] [rbp-6EEh]
  char v2791; // [rsp+DB3h] [rbp-6EDh]
  char v2792; // [rsp+DB4h] [rbp-6ECh]
  char v2793; // [rsp+DB5h] [rbp-6EBh]
  char v2794; // [rsp+DB6h] [rbp-6EAh]
  char v2795; // [rsp+DB7h] [rbp-6E9h]
  char v2796; // [rsp+DB8h] [rbp-6E8h]
  char v2797; // [rsp+DB9h] [rbp-6E7h]
  char v2798; // [rsp+DBAh] [rbp-6E6h]
  char v2799; // [rsp+DBBh] [rbp-6E5h]
  char v2800; // [rsp+DC0h] [rbp-6E0h] BYREF
  char v2801; // [rsp+DC1h] [rbp-6DFh]
  char v2802; // [rsp+DC2h] [rbp-6DEh]
  char v2803; // [rsp+DC3h] [rbp-6DDh]
  char v2804; // [rsp+DC4h] [rbp-6DCh]
  char v2805; // [rsp+DC5h] [rbp-6DBh]
  char v2806; // [rsp+DC6h] [rbp-6DAh]
  char v2807; // [rsp+DC7h] [rbp-6D9h]
  char v2808; // [rsp+DC8h] [rbp-6D8h]
  char v2809; // [rsp+DC9h] [rbp-6D7h]
  char v2810; // [rsp+DCAh] [rbp-6D6h]
  char v2811; // [rsp+DCBh] [rbp-6D5h]
  char v2812; // [rsp+DCCh] [rbp-6D4h]
  char v2813; // [rsp+DCDh] [rbp-6D3h]
  char v2814; // [rsp+DCEh] [rbp-6D2h]
  char v2815; // [rsp+DCFh] [rbp-6D1h]
  char v2816; // [rsp+DD0h] [rbp-6D0h]
  char v2817; // [rsp+DD1h] [rbp-6CFh]
  char v2818; // [rsp+DD2h] [rbp-6CEh]
  char v2819; // [rsp+DD3h] [rbp-6CDh]
  char v2820; // [rsp+DD4h] [rbp-6CCh]
  char v2821; // [rsp+DD5h] [rbp-6CBh]
  char v2822; // [rsp+DD6h] [rbp-6CAh]
  char v2823; // [rsp+DD7h] [rbp-6C9h]
  char v2824; // [rsp+DD8h] [rbp-6C8h]
  char v2825; // [rsp+DD9h] [rbp-6C7h]
  char v2826; // [rsp+DDAh] [rbp-6C6h]
  char v2827; // [rsp+DDBh] [rbp-6C5h]
  char v2828; // [rsp+DDCh] [rbp-6C4h]
  char v2829; // [rsp+DDDh] [rbp-6C3h]
  char v2830; // [rsp+DDEh] [rbp-6C2h]
  char v2831; // [rsp+DDFh] [rbp-6C1h]
  char v2832; // [rsp+DE0h] [rbp-6C0h]
  char v2833; // [rsp+DE1h] [rbp-6BFh]
  char v2834; // [rsp+DE2h] [rbp-6BEh]
  char v2835; // [rsp+DE3h] [rbp-6BDh]
  char v2836; // [rsp+DE4h] [rbp-6BCh]
  char v2837; // [rsp+DE5h] [rbp-6BBh]
  char v2838; // [rsp+DE6h] [rbp-6BAh]
  char v2839; // [rsp+DE7h] [rbp-6B9h]
  char v2840; // [rsp+DE8h] [rbp-6B8h]
  char v2841; // [rsp+DE9h] [rbp-6B7h]
  char v2842; // [rsp+DEAh] [rbp-6B6h]
  char v2843; // [rsp+DEBh] [rbp-6B5h]
  char v2844; // [rsp+DECh] [rbp-6B4h]
  char v2845; // [rsp+DEDh] [rbp-6B3h]
  char v2846; // [rsp+DEEh] [rbp-6B2h]
  char v2847; // [rsp+DEFh] [rbp-6B1h]
  char v2848; // [rsp+DF0h] [rbp-6B0h]
  char v2849; // [rsp+DF1h] [rbp-6AFh]
  char v2850; // [rsp+DF2h] [rbp-6AEh]
  char v2851; // [rsp+DF3h] [rbp-6ADh]
  char v2852; // [rsp+DF4h] [rbp-6ACh]
  char v2853; // [rsp+DF5h] [rbp-6ABh]
  char v2854; // [rsp+DF6h] [rbp-6AAh]
  char v2855; // [rsp+DF7h] [rbp-6A9h]
  char v2856; // [rsp+DF8h] [rbp-6A8h]
  char v2857; // [rsp+DF9h] [rbp-6A7h]
  char v2858; // [rsp+DFAh] [rbp-6A6h]
  char v2859; // [rsp+DFBh] [rbp-6A5h]
  char v2860; // [rsp+E00h] [rbp-6A0h] BYREF
  char v2861; // [rsp+E01h] [rbp-69Fh]
  char v2862; // [rsp+E02h] [rbp-69Eh]
  char v2863; // [rsp+E03h] [rbp-69Dh]
  char v2864; // [rsp+E04h] [rbp-69Ch]
  char v2865; // [rsp+E05h] [rbp-69Bh]
  char v2866; // [rsp+E06h] [rbp-69Ah]
  char v2867; // [rsp+E07h] [rbp-699h]
  char v2868; // [rsp+E08h] [rbp-698h]
  char v2869; // [rsp+E09h] [rbp-697h]
  char v2870; // [rsp+E0Ah] [rbp-696h]
  char v2871; // [rsp+E0Bh] [rbp-695h]
  char v2872; // [rsp+E0Ch] [rbp-694h]
  char v2873; // [rsp+E0Dh] [rbp-693h]
  char v2874; // [rsp+E0Eh] [rbp-692h]
  char v2875; // [rsp+E0Fh] [rbp-691h]
  char v2876; // [rsp+E10h] [rbp-690h]
  char v2877; // [rsp+E11h] [rbp-68Fh]
  char v2878; // [rsp+E12h] [rbp-68Eh]
  char v2879; // [rsp+E13h] [rbp-68Dh]
  char v2880; // [rsp+E14h] [rbp-68Ch]
  char v2881; // [rsp+E15h] [rbp-68Bh]
  char v2882; // [rsp+E16h] [rbp-68Ah]
  char v2883; // [rsp+E17h] [rbp-689h]
  char v2884; // [rsp+E18h] [rbp-688h]
  char v2885; // [rsp+E19h] [rbp-687h]
  char v2886; // [rsp+E1Ah] [rbp-686h]
  char v2887; // [rsp+E1Bh] [rbp-685h]
  char v2888; // [rsp+E1Ch] [rbp-684h]
  char v2889; // [rsp+E1Dh] [rbp-683h]
  char v2890; // [rsp+E1Eh] [rbp-682h]
  char v2891; // [rsp+E1Fh] [rbp-681h]
  char v2892; // [rsp+E20h] [rbp-680h]
  char v2893; // [rsp+E21h] [rbp-67Fh]
  char v2894; // [rsp+E22h] [rbp-67Eh]
  char v2895; // [rsp+E23h] [rbp-67Dh]
  char v2896; // [rsp+E24h] [rbp-67Ch]
  char v2897; // [rsp+E25h] [rbp-67Bh]
  char v2898; // [rsp+E26h] [rbp-67Ah]
  char v2899; // [rsp+E27h] [rbp-679h]
  char v2900; // [rsp+E28h] [rbp-678h]
  char v2901; // [rsp+E29h] [rbp-677h]
  char v2902; // [rsp+E2Ah] [rbp-676h]
  char v2903; // [rsp+E2Bh] [rbp-675h]
  char v2904; // [rsp+E2Ch] [rbp-674h]
  char v2905; // [rsp+E2Dh] [rbp-673h]
  char v2906; // [rsp+E2Eh] [rbp-672h]
  char v2907; // [rsp+E30h] [rbp-670h]
  char v2908; // [rsp+E31h] [rbp-66Fh]
  char v2909; // [rsp+E32h] [rbp-66Eh]
  char v2910; // [rsp+E33h] [rbp-66Dh]
  char v2911; // [rsp+E34h] [rbp-66Ch]
  char v2912; // [rsp+E35h] [rbp-66Bh]
  char v2913; // [rsp+E36h] [rbp-66Ah]
  char v2914; // [rsp+E37h] [rbp-669h]
  char v2915; // [rsp+E38h] [rbp-668h]
  char v2916; // [rsp+E39h] [rbp-667h]
  char v2917; // [rsp+E3Ah] [rbp-666h]
  char v2918; // [rsp+E3Bh] [rbp-665h]
  char v2919; // [rsp+E40h] [rbp-660h] BYREF
  char v2920; // [rsp+E41h] [rbp-65Fh]
  char v2921; // [rsp+E42h] [rbp-65Eh]
  char v2922; // [rsp+E43h] [rbp-65Dh]
  char v2923; // [rsp+E44h] [rbp-65Ch]
  char v2924; // [rsp+E45h] [rbp-65Bh]
  char v2925; // [rsp+E46h] [rbp-65Ah]
  char v2926; // [rsp+E47h] [rbp-659h]
  char v2927; // [rsp+E48h] [rbp-658h]
  char v2928; // [rsp+E49h] [rbp-657h]
  char v2929; // [rsp+E4Ah] [rbp-656h]
  char v2930; // [rsp+E4Bh] [rbp-655h]
  char v2931; // [rsp+E4Ch] [rbp-654h]
  char v2932; // [rsp+E4Dh] [rbp-653h]
  char v2933; // [rsp+E4Eh] [rbp-652h]
  char v2934; // [rsp+E4Fh] [rbp-651h]
  char v2935; // [rsp+E50h] [rbp-650h]
  char v2936; // [rsp+E51h] [rbp-64Fh]
  char v2937; // [rsp+E52h] [rbp-64Eh]
  char v2938; // [rsp+E53h] [rbp-64Dh]
  char v2939; // [rsp+E54h] [rbp-64Ch]
  char v2940; // [rsp+E55h] [rbp-64Bh]
  char v2941; // [rsp+E56h] [rbp-64Ah]
  char v2942; // [rsp+E57h] [rbp-649h]
  char v2943; // [rsp+E58h] [rbp-648h]
  char v2944; // [rsp+E59h] [rbp-647h]
  char v2945; // [rsp+E5Ah] [rbp-646h]
  char v2946; // [rsp+E5Bh] [rbp-645h]
  char v2947; // [rsp+E5Ch] [rbp-644h]
  char v2948; // [rsp+E5Dh] [rbp-643h]
  char v2949; // [rsp+E5Eh] [rbp-642h]
  char v2950; // [rsp+E5Fh] [rbp-641h]
  char v2951; // [rsp+E60h] [rbp-640h]
  char v2952; // [rsp+E61h] [rbp-63Fh]
  char v2953; // [rsp+E62h] [rbp-63Eh]
  char v2954; // [rsp+E63h] [rbp-63Dh]
  char v2955; // [rsp+E64h] [rbp-63Ch]
  char v2956; // [rsp+E65h] [rbp-63Bh]
  char v2957; // [rsp+E66h] [rbp-63Ah]
  char v2958; // [rsp+E67h] [rbp-639h]
  char v2959; // [rsp+E68h] [rbp-638h]
  char v2960; // [rsp+E69h] [rbp-637h]
  char v2961; // [rsp+E6Ah] [rbp-636h]
  char v2962; // [rsp+E6Bh] [rbp-635h]
  char v2963; // [rsp+E6Ch] [rbp-634h]
  char v2964; // [rsp+E6Dh] [rbp-633h]
  char v2965; // [rsp+E6Eh] [rbp-632h]
  char v2966; // [rsp+E6Fh] [rbp-631h]
  char v2967; // [rsp+E70h] [rbp-630h]
  char v2968; // [rsp+E71h] [rbp-62Fh]
  char v2969; // [rsp+E72h] [rbp-62Eh]
  char v2970; // [rsp+E73h] [rbp-62Dh]
  char v2971; // [rsp+E74h] [rbp-62Ch]
  char v2972; // [rsp+E75h] [rbp-62Bh]
  char v2973; // [rsp+E76h] [rbp-62Ah]
  char v2974; // [rsp+E77h] [rbp-629h]
  char v2975; // [rsp+E78h] [rbp-628h]
  char v2976; // [rsp+E79h] [rbp-627h]
  char v2977; // [rsp+E7Ah] [rbp-626h]
  char v2978; // [rsp+E7Bh] [rbp-625h]
  int v2979; // [rsp+E80h] [rbp-620h]
  int v2980; // [rsp+E84h] [rbp-61Ch]
  int v2981; // [rsp+E88h] [rbp-618h]
  int v2982; // [rsp+E8Ch] [rbp-614h]
  int v2983; // [rsp+E90h] [rbp-610h]
  int v2984; // [rsp+EA0h] [rbp-600h]
  int v2985; // [rsp+EA4h] [rbp-5FCh]
  int v2986; // [rsp+EA8h] [rbp-5F8h]
  int v2987; // [rsp+EACh] [rbp-5F4h]
  int v2988; // [rsp+EB0h] [rbp-5F0h]
  int v2989; // [rsp+EB4h] [rbp-5ECh]
  int v2990; // [rsp+EB8h] [rbp-5E8h]
  int v2991; // [rsp+EC0h] [rbp-5E0h]
  int v2992; // [rsp+EC4h] [rbp-5DCh]
  int v2993; // [rsp+EC8h] [rbp-5D8h]
  int v2994; // [rsp+ECCh] [rbp-5D4h]
  int v2995; // [rsp+ED0h] [rbp-5D0h]
  int v2996; // [rsp+ED4h] [rbp-5CCh]
  int v2997; // [rsp+EE0h] [rbp-5C0h]
  int v2998; // [rsp+EE4h] [rbp-5BCh]
  int v2999; // [rsp+EE8h] [rbp-5B8h]
  int v3000; // [rsp+EECh] [rbp-5B4h]
  int v3001; // [rsp+EF0h] [rbp-5B0h]
  int v3002; // [rsp+EF4h] [rbp-5ACh]
  int v3003; // [rsp+EF8h] [rbp-5A8h]
  int v3004; // [rsp+F00h] [rbp-5A0h]
  int v3005; // [rsp+F04h] [rbp-59Ch]
  int v3006; // [rsp+F08h] [rbp-598h]
  int v3007; // [rsp+F0Ch] [rbp-594h]
  int v3008; // [rsp+F10h] [rbp-590h]
  int v3009; // [rsp+F14h] [rbp-58Ch]
  int v3010; // [rsp+F18h] [rbp-588h]
  int v3011; // [rsp+F20h] [rbp-580h]
  int v3012; // [rsp+F24h] [rbp-57Ch]
  int v3013; // [rsp+F28h] [rbp-578h]
  int v3014; // [rsp+F2Ch] [rbp-574h]
  int v3015; // [rsp+F30h] [rbp-570h]
  int v3016; // [rsp+F34h] [rbp-56Ch]
  int v3017; // [rsp+F38h] [rbp-568h]
  int v3018; // [rsp+F40h] [rbp-560h]
  int v3019; // [rsp+F44h] [rbp-55Ch]
  int v3020; // [rsp+F48h] [rbp-558h]
  int v3021; // [rsp+F4Ch] [rbp-554h]
  int v3022; // [rsp+F50h] [rbp-550h]
  int v3023; // [rsp+F54h] [rbp-54Ch]
  int v3024; // [rsp+F58h] [rbp-548h]
  int v3025; // [rsp+F60h] [rbp-540h]
  int v3026; // [rsp+F64h] [rbp-53Ch]
  int v3027; // [rsp+F68h] [rbp-538h]
  int v3028; // [rsp+F6Ch] [rbp-534h]
  int v3029; // [rsp+F70h] [rbp-530h]
  int v3030; // [rsp+F74h] [rbp-52Ch]
  int v3031; // [rsp+F78h] [rbp-528h]
  int v3032; // [rsp+F7Ch] [rbp-524h]
  int v3033; // [rsp+F80h] [rbp-520h]
  int v3034; // [rsp+F90h] [rbp-510h]
  int v3035; // [rsp+F94h] [rbp-50Ch]
  int v3036; // [rsp+F98h] [rbp-508h]
  int v3037; // [rsp+F9Ch] [rbp-504h]
  int v3038; // [rsp+FA0h] [rbp-500h]
  int v3039; // [rsp+FA4h] [rbp-4FCh]
  int v3040; // [rsp+FA8h] [rbp-4F8h]
  int v3041; // [rsp+FACh] [rbp-4F4h]
  int v3042; // [rsp+FB0h] [rbp-4F0h]
  int v3043; // [rsp+FC0h] [rbp-4E0h]
  int v3044; // [rsp+FC4h] [rbp-4DCh]
  int v3045; // [rsp+FC8h] [rbp-4D8h]
  int v3046; // [rsp+FCCh] [rbp-4D4h]
  int v3047; // [rsp+FD0h] [rbp-4D0h]
  int v3048; // [rsp+FD4h] [rbp-4CCh]
  int v3049; // [rsp+FD8h] [rbp-4C8h]
  int v3050; // [rsp+FDCh] [rbp-4C4h]
  int v3051; // [rsp+FE0h] [rbp-4C0h]
  int v3052; // [rsp+FE4h] [rbp-4BCh]
  int v3053; // [rsp+FE8h] [rbp-4B8h]
  int v3054; // [rsp+FF0h] [rbp-4B0h]
  int v3055; // [rsp+FF4h] [rbp-4ACh]
  int v3056; // [rsp+FF8h] [rbp-4A8h]
  int v3057; // [rsp+FFCh] [rbp-4A4h]
  int v3058; // [rsp+1000h] [rbp-4A0h]
  int v3059; // [rsp+1004h] [rbp-49Ch]
  int v3060; // [rsp+1008h] [rbp-498h]
  int v3061; // [rsp+100Ch] [rbp-494h]
  int v3062; // [rsp+1010h] [rbp-490h]
  int v3063; // [rsp+1020h] [rbp-480h]
  int v3064; // [rsp+1024h] [rbp-47Ch]
  int v3065; // [rsp+1028h] [rbp-478h]
  int v3066; // [rsp+102Ch] [rbp-474h]
  int v3067; // [rsp+1030h] [rbp-470h]
  int v3068; // [rsp+1040h] [rbp-460h]
  int v3069; // [rsp+1044h] [rbp-45Ch]
  int v3070; // [rsp+1048h] [rbp-458h]
  int v3071; // [rsp+104Ch] [rbp-454h]
  int v3072; // [rsp+1050h] [rbp-450h]
  int v3073; // [rsp+1054h] [rbp-44Ch]
  int v3074; // [rsp+1058h] [rbp-448h]
  int v3075; // [rsp+105Ch] [rbp-444h]
  int v3076; // [rsp+1060h] [rbp-440h]
  int v3077; // [rsp+1064h] [rbp-43Ch]
  int v3078; // [rsp+1068h] [rbp-438h]
  int v3079; // [rsp+106Ch] [rbp-434h]
  int v3080; // [rsp+1070h] [rbp-430h]
  int v3081; // [rsp+1074h] [rbp-42Ch]
  int v3082; // [rsp+1078h] [rbp-428h]
  int v3083; // [rsp+1080h] [rbp-420h]
  int v3084; // [rsp+1084h] [rbp-41Ch]
  int v3085; // [rsp+1088h] [rbp-418h]
  int v3086; // [rsp+108Ch] [rbp-414h]
  int v3087; // [rsp+1090h] [rbp-410h]
  int v3088; // [rsp+10A0h] [rbp-400h]
  int v3089; // [rsp+10A4h] [rbp-3FCh]
  int v3090; // [rsp+10A8h] [rbp-3F8h]
  int v3091; // [rsp+10ACh] [rbp-3F4h]
  int v3092; // [rsp+10B0h] [rbp-3F0h]
  int v3093; // [rsp+10B4h] [rbp-3ECh]
  int v3094; // [rsp+10C0h] [rbp-3E0h]
  int v3095; // [rsp+10C4h] [rbp-3DCh]
  int v3096; // [rsp+10C8h] [rbp-3D8h]
  int v3097; // [rsp+10CCh] [rbp-3D4h]
  int v3098; // [rsp+10D0h] [rbp-3D0h]
  int v3099; // [rsp+10E0h] [rbp-3C0h]
  int v3100; // [rsp+10E4h] [rbp-3BCh]
  int v3101; // [rsp+10E8h] [rbp-3B8h]
  int v3102; // [rsp+10ECh] [rbp-3B4h]
  int v3103; // [rsp+10F0h] [rbp-3B0h]
  int v3104; // [rsp+10F4h] [rbp-3ACh]
  int v3105; // [rsp+10F8h] [rbp-3A8h]
  int v3106; // [rsp+1100h] [rbp-3A0h]
  int v3107; // [rsp+1104h] [rbp-39Ch]
  int v3108; // [rsp+1108h] [rbp-398h]
  int v3109; // [rsp+110Ch] [rbp-394h]
  int v3110; // [rsp+1110h] [rbp-390h]
  int v3111; // [rsp+1114h] [rbp-38Ch]
  int v3112; // [rsp+1118h] [rbp-388h]
  int v3113; // [rsp+1120h] [rbp-380h]
  int v3114; // [rsp+1124h] [rbp-37Ch]
  int v3115; // [rsp+1128h] [rbp-378h]
  int v3116; // [rsp+112Ch] [rbp-374h]
  int v3117; // [rsp+1130h] [rbp-370h]
  int v3118; // [rsp+1140h] [rbp-360h]
  int v3119; // [rsp+1144h] [rbp-35Ch]
  int v3120; // [rsp+1148h] [rbp-358h]
  int v3121; // [rsp+114Ch] [rbp-354h]
  int v3122; // [rsp+1150h] [rbp-350h]
  int v3123; // [rsp+1160h] [rbp-340h]
  int v3124; // [rsp+1164h] [rbp-33Ch]
  int v3125; // [rsp+1168h] [rbp-338h]
  int v3126; // [rsp+116Ch] [rbp-334h]
  int v3127; // [rsp+1170h] [rbp-330h]
  int v3128; // [rsp+1180h] [rbp-320h]
  int v3129; // [rsp+1184h] [rbp-31Ch]
  int v3130; // [rsp+1188h] [rbp-318h]
  int v3131; // [rsp+118Ch] [rbp-314h]
  int v3132; // [rsp+1190h] [rbp-310h]
  int v3133; // [rsp+1194h] [rbp-30Ch]
  int v3134; // [rsp+1198h] [rbp-308h]
  int v3135; // [rsp+119Ch] [rbp-304h]
  int v3136; // [rsp+11A0h] [rbp-300h]
  int v3137; // [rsp+11A4h] [rbp-2FCh]
  int v3138; // [rsp+11A8h] [rbp-2F8h]
  int v3139; // [rsp+11B0h] [rbp-2F0h]
  int v3140; // [rsp+11B4h] [rbp-2ECh]
  int v3141; // [rsp+11B8h] [rbp-2E8h]
  int v3142; // [rsp+11BCh] [rbp-2E4h]
  int v3143; // [rsp+11C0h] [rbp-2E0h]
  int v3144; // [rsp+11C4h] [rbp-2DCh]
  int v3145; // [rsp+11C8h] [rbp-2D8h]
  int v3146; // [rsp+11D0h] [rbp-2D0h]
  int v3147; // [rsp+11D4h] [rbp-2CCh]
  int v3148; // [rsp+11D8h] [rbp-2C8h]
  int v3149; // [rsp+11DCh] [rbp-2C4h]
  int v3150; // [rsp+11E0h] [rbp-2C0h]
  int v3151; // [rsp+11E4h] [rbp-2BCh]
  int v3152; // [rsp+11E8h] [rbp-2B8h]
  int v3153; // [rsp+11F0h] [rbp-2B0h]
  int v3154; // [rsp+11F4h] [rbp-2ACh]
  int v3155; // [rsp+11F8h] [rbp-2A8h]
  int v3156; // [rsp+11FCh] [rbp-2A4h]
  int v3157; // [rsp+1200h] [rbp-2A0h]
  int v3158; // [rsp+1210h] [rbp-290h]
  int v3159; // [rsp+1214h] [rbp-28Ch]
  int v3160; // [rsp+1218h] [rbp-288h]
  int v3161; // [rsp+121Ch] [rbp-284h]
  char v3162; // [rsp+1220h] [rbp-280h] BYREF
  char v3163; // [rsp+1221h] [rbp-27Fh]
  char v3164; // [rsp+1222h] [rbp-27Eh]
  char v3165; // [rsp+1223h] [rbp-27Dh]
  char v3166; // [rsp+1224h] [rbp-27Ch]
  char v3167; // [rsp+1225h] [rbp-27Bh]
  char v3168; // [rsp+1226h] [rbp-27Ah]
  char v3169; // [rsp+1227h] [rbp-279h]
  char v3170; // [rsp+1228h] [rbp-278h]
  char v3171; // [rsp+1229h] [rbp-277h]
  char v3172; // [rsp+122Ah] [rbp-276h]
  char v3173; // [rsp+122Bh] [rbp-275h]
  char v3174; // [rsp+122Ch] [rbp-274h]
  char v3175; // [rsp+122Dh] [rbp-273h]
  char v3176; // [rsp+122Eh] [rbp-272h]
  char v3177; // [rsp+122Fh] [rbp-271h]
  char v3178; // [rsp+1230h] [rbp-270h]
  char v3179; // [rsp+1231h] [rbp-26Fh]
  char v3180; // [rsp+1232h] [rbp-26Eh]
  char v3181; // [rsp+1233h] [rbp-26Dh]
  char v3182; // [rsp+1234h] [rbp-26Ch]
  char v3183; // [rsp+1235h] [rbp-26Bh]
  char v3184; // [rsp+1236h] [rbp-26Ah]
  char v3185; // [rsp+1237h] [rbp-269h]
  char v3186; // [rsp+1238h] [rbp-268h]
  char v3187; // [rsp+1239h] [rbp-267h]
  char v3188; // [rsp+123Ah] [rbp-266h]
  char v3189; // [rsp+123Bh] [rbp-265h]
  char v3190; // [rsp+123Ch] [rbp-264h]
  char v3191; // [rsp+123Dh] [rbp-263h]
  int v3192; // [rsp+1240h] [rbp-260h]
  int v3193; // [rsp+1244h] [rbp-25Ch]
  int v3194; // [rsp+1248h] [rbp-258h]
  int v3195; // [rsp+124Ch] [rbp-254h]
  int v3196; // [rsp+1250h] [rbp-250h]
  int v3197; // [rsp+1254h] [rbp-24Ch]
  int v3198; // [rsp+1260h] [rbp-240h]
  int v3199; // [rsp+1264h] [rbp-23Ch]
  int v3200; // [rsp+1268h] [rbp-238h]
  int v3201; // [rsp+126Ch] [rbp-234h]
  int v3202; // [rsp+1270h] [rbp-230h]
  int v3203; // [rsp+1274h] [rbp-22Ch]
  int v3204; // [rsp+1278h] [rbp-228h]
  int v3205; // [rsp+127Ch] [rbp-224h]
  int v3206; // [rsp+1280h] [rbp-220h]
  int v3207; // [rsp+1284h] [rbp-21Ch]
  int v3208; // [rsp+1290h] [rbp-210h]
  int v3209; // [rsp+1294h] [rbp-20Ch]
  int v3210; // [rsp+1298h] [rbp-208h]
  int v3211; // [rsp+129Ch] [rbp-204h]
  int v3212; // [rsp+12A0h] [rbp-200h]
  int v3213; // [rsp+12A4h] [rbp-1FCh]
  char v3214; // [rsp+12B0h] [rbp-1F0h] BYREF
  char v3215; // [rsp+12B1h] [rbp-1EFh]
  char v3216; // [rsp+12B2h] [rbp-1EEh]
  char v3217; // [rsp+12B3h] [rbp-1EDh]
  char v3218; // [rsp+12B4h] [rbp-1ECh]
  char v3219; // [rsp+12B5h] [rbp-1EBh]
  char v3220; // [rsp+12B6h] [rbp-1EAh]
  char v3221; // [rsp+12B7h] [rbp-1E9h]
  char v3222; // [rsp+12B8h] [rbp-1E8h]
  char v3223; // [rsp+12B9h] [rbp-1E7h]
  char v3224; // [rsp+12BAh] [rbp-1E6h]
  char v3225; // [rsp+12BBh] [rbp-1E5h]
  char v3226; // [rsp+12BCh] [rbp-1E4h]
  char v3227; // [rsp+12BDh] [rbp-1E3h]
  char v3228; // [rsp+12BEh] [rbp-1E2h]
  char v3229; // [rsp+12BFh] [rbp-1E1h]
  char v3230; // [rsp+12C0h] [rbp-1E0h]
  char v3231; // [rsp+12C1h] [rbp-1DFh]
  char v3232; // [rsp+12C2h] [rbp-1DEh]
  char v3233; // [rsp+12C3h] [rbp-1DDh]
  char v3234; // [rsp+12C4h] [rbp-1DCh]
  char v3235; // [rsp+12C5h] [rbp-1DBh]
  char v3236; // [rsp+12C6h] [rbp-1DAh]
  char v3237; // [rsp+12C7h] [rbp-1D9h]
  char v3238; // [rsp+12C8h] [rbp-1D8h]
  char v3239; // [rsp+12C9h] [rbp-1D7h]
  char v3240; // [rsp+12CAh] [rbp-1D6h]
  char v3241; // [rsp+12CBh] [rbp-1D5h]
  char v3242; // [rsp+12CCh] [rbp-1D4h]
  char v3243; // [rsp+12CDh] [rbp-1D3h]
  char v3244; // [rsp+12CEh] [rbp-1D2h]
  int v3245; // [rsp+12D0h] [rbp-1D0h]
  int v3246; // [rsp+12D4h] [rbp-1CCh]
  int v3247; // [rsp+12D8h] [rbp-1C8h]
  int v3248; // [rsp+12DCh] [rbp-1C4h]
  int v3249; // [rsp+12E0h] [rbp-1C0h]
  int v3250; // [rsp+12E4h] [rbp-1BCh]
  char v3251; // [rsp+12F0h] [rbp-1B0h] BYREF
  char v3252; // [rsp+12F1h] [rbp-1AFh]
  char v3253; // [rsp+12F2h] [rbp-1AEh]
  char v3254; // [rsp+12F3h] [rbp-1ADh]
  char v3255; // [rsp+12F4h] [rbp-1ACh]
  char v3256; // [rsp+12F5h] [rbp-1ABh]
  char v3257; // [rsp+12F6h] [rbp-1AAh]
  char v3258; // [rsp+12F7h] [rbp-1A9h]
  char v3259; // [rsp+12F8h] [rbp-1A8h]
  char v3260; // [rsp+12F9h] [rbp-1A7h]
  char v3261; // [rsp+12FAh] [rbp-1A6h]
  char v3262; // [rsp+12FBh] [rbp-1A5h]
  char v3263; // [rsp+12FCh] [rbp-1A4h]
  char v3264; // [rsp+12FDh] [rbp-1A3h]
  char v3265; // [rsp+12FEh] [rbp-1A2h]
  char v3266; // [rsp+12FFh] [rbp-1A1h]
  char v3267; // [rsp+1300h] [rbp-1A0h]
  char v3268; // [rsp+1301h] [rbp-19Fh]
  char v3269; // [rsp+1302h] [rbp-19Eh]
  char v3270; // [rsp+1303h] [rbp-19Dh]
  char v3271; // [rsp+1304h] [rbp-19Ch]
  char v3272; // [rsp+1305h] [rbp-19Bh]
  char v3273; // [rsp+1306h] [rbp-19Ah]
  char v3274; // [rsp+1307h] [rbp-199h]
  char v3275; // [rsp+1308h] [rbp-198h]
  char v3276; // [rsp+1309h] [rbp-197h]
  char v3277; // [rsp+130Ah] [rbp-196h]
  char v3278; // [rsp+130Bh] [rbp-195h]
  char v3279; // [rsp+130Ch] [rbp-194h]
  char v3280; // [rsp+130Dh] [rbp-193h]
  char v3281; // [rsp+130Eh] [rbp-192h]
  int v3282; // [rsp+1310h] [rbp-190h]
  int v3283; // [rsp+1314h] [rbp-18Ch]
  int v3284; // [rsp+1318h] [rbp-188h]
  int v3285; // [rsp+131Ch] [rbp-184h]
  int v3286; // [rsp+1320h] [rbp-180h]
  int v3287; // [rsp+1330h] [rbp-170h]
  int v3288; // [rsp+1334h] [rbp-16Ch]
  int v3289; // [rsp+1338h] [rbp-168h]
  int v3290; // [rsp+133Ch] [rbp-164h]
  int v3291; // [rsp+1340h] [rbp-160h]
  int v3292; // [rsp+1344h] [rbp-15Ch]
  int v3293; // [rsp+1348h] [rbp-158h]
  int v3294; // [rsp+134Ch] [rbp-154h]
  int v3295; // [rsp+1350h] [rbp-150h]
  int v3296; // [rsp+1354h] [rbp-14Ch]
  int v3297; // [rsp+1358h] [rbp-148h]
  int v3298; // [rsp+1360h] [rbp-140h]
  int v3299; // [rsp+1364h] [rbp-13Ch]
  int v3300; // [rsp+1368h] [rbp-138h]
  int v3301; // [rsp+136Ch] [rbp-134h]
  int v3302; // [rsp+1370h] [rbp-130h]
  int v3303; // [rsp+1380h] [rbp-120h]
  int v3304; // [rsp+1384h] [rbp-11Ch]
  int v3305; // [rsp+1388h] [rbp-118h]
  int v3306; // [rsp+138Ch] [rbp-114h]
  int v3307; // [rsp+1390h] [rbp-110h]
  int v3308; // [rsp+1394h] [rbp-10Ch]
  int v3309; // [rsp+1398h] [rbp-108h]
  int v3310; // [rsp+13A0h] [rbp-100h]
  int v3311; // [rsp+13A4h] [rbp-FCh]
  int v3312; // [rsp+13A8h] [rbp-F8h]
  int v3313; // [rsp+13ACh] [rbp-F4h]
  int v3314; // [rsp+13B0h] [rbp-F0h]
  int v3315; // [rsp+13C0h] [rbp-E0h]
  int v3316; // [rsp+13C4h] [rbp-DCh]
  int v3317; // [rsp+13C8h] [rbp-D8h]
  int v3318; // [rsp+13CCh] [rbp-D4h]
  int v3319; // [rsp+13D0h] [rbp-D0h]
  int v3320; // [rsp+13D4h] [rbp-CCh]
  int v3321; // [rsp+13D8h] [rbp-C8h]
  int v3322; // [rsp+13E0h] [rbp-C0h]
  int v3323; // [rsp+13E4h] [rbp-BCh]
  int v3324; // [rsp+13E8h] [rbp-B8h]
  int v3325; // [rsp+13ECh] [rbp-B4h]
  char v3326; // [rsp+13F0h] [rbp-B0h] BYREF
  char v3327; // [rsp+13F1h] [rbp-AFh]
  char v3328; // [rsp+13F2h] [rbp-AEh]
  char v3329; // [rsp+13F3h] [rbp-ADh]
  char v3330; // [rsp+13F4h] [rbp-ACh]
  char v3331; // [rsp+13F5h] [rbp-ABh]
  char v3332; // [rsp+13F6h] [rbp-AAh]
  char v3333; // [rsp+13F7h] [rbp-A9h]
  char v3334; // [rsp+13F8h] [rbp-A8h]
  char v3335; // [rsp+13F9h] [rbp-A7h]
  char v3336; // [rsp+13FAh] [rbp-A6h]
  char v3337; // [rsp+13FBh] [rbp-A5h]
  char v3338; // [rsp+13FCh] [rbp-A4h]
  char v3339; // [rsp+13FDh] [rbp-A3h]
  char v3340; // [rsp+13FEh] [rbp-A2h]
  char v3341; // [rsp+13FFh] [rbp-A1h]
  char v3342; // [rsp+1400h] [rbp-A0h]
  char v3343; // [rsp+1401h] [rbp-9Fh]
  char v3344; // [rsp+1402h] [rbp-9Eh]
  char v3345; // [rsp+1403h] [rbp-9Dh]
  char v3346; // [rsp+1404h] [rbp-9Ch]
  char v3347; // [rsp+1405h] [rbp-9Bh]
  char v3348; // [rsp+1406h] [rbp-9Ah]
  char v3349; // [rsp+1407h] [rbp-99h]
  char v3350; // [rsp+1408h] [rbp-98h]
  char v3351; // [rsp+1409h] [rbp-97h]
  char v3352; // [rsp+140Ah] [rbp-96h]
  char v3353; // [rsp+140Bh] [rbp-95h]
  char v3354; // [rsp+140Ch] [rbp-94h]
  char v3355; // [rsp+140Dh] [rbp-93h]
  char v3356; // [rsp+140Eh] [rbp-92h]
  int v3357; // [rsp+1410h] [rbp-90h]
  int v3358; // [rsp+1414h] [rbp-8Ch]
  int v3359; // [rsp+1418h] [rbp-88h]
  int v3360; // [rsp+141Ch] [rbp-84h]
  int v3361; // [rsp+1420h] [rbp-80h]
  int v3362; // [rsp+1430h] [rbp-70h]
  int v3363; // [rsp+1434h] [rbp-6Ch]
  int v3364; // [rsp+1438h] [rbp-68h]
  int v3365; // [rsp+143Ch] [rbp-64h]
  int v3366; // [rsp+1440h] [rbp-60h]
  int v3367; // [rsp+1444h] [rbp-5Ch]
  int v3368; // [rsp+1450h] [rbp-50h]
  int v3369; // [rsp+1454h] [rbp-4Ch]
  int v3370; // [rsp+1458h] [rbp-48h]
  int v3371; // [rsp+145Ch] [rbp-44h]
  int v3372; // [rsp+1460h] [rbp-40h]
  int v3373; // [rsp+1464h] [rbp-3Ch]
  int v3374; // [rsp+1468h] [rbp-38h]
  int v3375; // [rsp+1470h] [rbp-30h]
  int v3376; // [rsp+1474h] [rbp-2Ch]
  int v3377; // [rsp+1478h] [rbp-28h]
  int v3378; // [rsp+147Ch] [rbp-24h]
  int v3379; // [rsp+1480h] [rbp-20h]
  int v3380; // [rsp+1484h] [rbp-1Ch]
  char v3381; // [rsp+1496h] [rbp-Ah] BYREF
  char v3382; // [rsp+1497h] [rbp-9h]
  char v3383; // [rsp+1498h] [rbp-8h]
  char v3384; // [rsp+149Bh] [rbp-5h]
  char v3385; // [rsp+149Ch] [rbp-4h]
  char v3386; // [rsp+149Dh] [rbp-3h]

  init();
  printf("uYhESoceNJGkMMFcmjd:");
  input_line(&v2118, 0x35uLL);
  v2138 ^= 0xDCu;
  v2161 ^= 0xC2u;
  v2127 ^= 0x8Bu;
  v2169 = ~v2169;
  v2144 ^= 0x88u;
  v2153 ^= 0xC3u;
  v2160 ^= 0x18u;
  v2143 ^= 0x91u;
  v2155 ^= 0xE9u;
  v2154 ^= 0x99u;
  v2133 ^= 0xADu;
  v2158 ^= 0x3Au;
  v2135 ^= 0x62u;
  v2166 ^= 0x6Au;
  v2137 ^= 0x57u;
  v2157 ^= 0x54u;
  v2120 ^= 0xFAu;
  v2145 ^= 0x74u;
  v2119 ^= 0xFAu;
  v2162 ^= 0x87u;
  v2151 ^= 0xA5u;
  v2148 ^= 0x80u;
  v2152 ^= 0x6Eu;
  v2146 ^= 4u;
  v2118 ^= 0x91u;
  v2139 ^= 0x91u;
  v2136 ^= 0xB8u;
  v2129 ^= 0xA7u;
  v2123 ^= 0x4Du;
  v2134 ^= 0xD9u;
  v2150 ^= 0xEu;
  v2159 ^= 0xF9u;
  v2156 ^= 0xF7u;
  v2131 ^= 0x7Cu;
  v2140 ^= 0x16u;
  v2122 ^= 0xA6u;
  v2124 ^= 0xF5u;
  v2128 ^= 0x2Fu;
  v2168 ^= 0x71u;
  v2142 ^= 0x7Bu;
  v2126 ^= 0x6Au;
  v2167 ^= 0x75u;
  v2130 ^= 0x84u;
  v2121 ^= 0x77u;
  v2163 ^= 0xFBu;
  v2125 ^= 0xB4u;
  v2164 ^= 0x78u;
  v2149 ^= 0x8Du;
  v2147 ^= 0xC7u;
  v2132 ^= 0xB6u;
  v2141 ^= 0xACu;
  v2165 ^= 0xF2u;
  if ( (unsigned int)fksth(&v2118, "erBDJvOroQgOOltKyWMCDpNPlskEHnSundKcbkzcSECamhyzRcNYS") )
  {
    printf("lxeaxqgvADxU:");
    input_line(&v2448, 0x3AuLL);
    v2474 ^= 0x74u;
    v2495 ^= 0x61u;
    v2492 ^= 0x34u;
    v2484 ^= 0xC2u;
    v2462 ^= 0x88u;
    v2455 ^= 0xC4u;
    v2480 ^= 0x44u;
    v2487 ^= 0xA7u;
    v2501 ^= 0x74u;
    v2481 ^= 0x8Au;
    v2472 ^= 0xAu;
    v2468 ^= 0xC3u;
    v2452 ^= 0x20u;
    v2448 ^= 0xBFu;
    v2498 ^= 0x60u;
    v2470 ^= 0xCDu;
    v2490 ^= 0xBDu;
    v2461 ^= 0xC0u;
    v2482 ^= 0xD6u;
    v2499 ^= 0xA2u;
    v2454 ^= 0x23u;
    v2476 ^= 0x35u;
    v2464 ^= 0xF1u;
    v2503 ^= 0xD3u;
    v2456 ^= 0x3Eu;
    v2467 ^= 0xD9u;
    v2479 ^= 0x94u;
    v2453 ^= 0xF8u;
    v2483 ^= 0x89u;
    v2466 ^= 0x7Du;
    v2477 ^= 0x96u;
    v2460 ^= 0xCDu;
    v2478 ^= 0x50u;
    v2450 ^= 0x52u;
    v2488 ^= 0xDu;
    v2497 ^= 0x50u;
    v2494 ^= 0x24u;
    v2457 ^= 0x5Cu;
    v2493 ^= 0x25u;
    v2458 ^= 0x80u;
    v2491 ^= 0x76u;
    v2469 ^= 0xEBu;
    v2485 ^= 0xD5u;
    v2463 ^= 2u;
    v2459 ^= 0xD4u;
    v2486 ^= 0x39u;
    v2471 ^= 0x4Eu;
    v2502 ^= 0xBCu;
    v2475 ^= 0x1Eu;
    v2451 ^= 0xBFu;
    v2473 ^= 0xEAu;
    v2465 ^= 0x90u;
    v2500 ^= 0xAu;
    v2496 ^= 0x65u;
    v2504 ^= 0xF5u;
    v2489 ^= 0x51u;
    v2449 ^= 0x8Du;
    v2505 ^= 0x81u;
    if ( (unsigned int)fksth(&v2448, "IszDnxOYlZTvaDWGGqlEEOKfwxdzdZTmCmcnXmqQJoAByFzCeHtCmlpVPh") )
    {
      printf("uwMGpwrBDSWe:");
      input_line(&v1350, 0x2DuLL);
      v1374 ^= 0x27u;
      v1373 ^= 0x1Fu;
      v1369 ^= 0x14u;
      v1368 ^= 0x45u;
      v1356 ^= 0x27u;
      v1361 ^= 0x6Du;
      v1393 ^= 0x3Du;
      v1350 ^= 0x57u;
      v1392 ^= 0x99u;
      v1383 ^= 0x87u;
      v1357 ^= 0xD8u;
      v1389 ^= 0x58u;
      v1351 ^= 0xA9u;
      v1391 ^= 0x39u;
      v1362 ^= 0xC8u;
      v1387 ^= 0xC8u;
      v1359 ^= 0x6Eu;
      v1375 ^= 0xA6u;
      v1385 ^= 0x99u;
      v1386 ^= 0x40u;
      v1367 ^= 0x88u;
      v1380 ^= 0x46u;
      v1354 ^= 0x8Cu;
      v1366 ^= 0xF5u;
      v1363 ^= 0x1Du;
      v1381 ^= 0x85u;
      v1378 ^= 0x8Eu;
      v1384 ^= 0x6Eu;
      v1376 ^= 0x1Au;
      v1371 ^= 0xD3u;
      v1360 ^= 0xA1u;
      v1388 ^= 0x23u;
      v1353 ^= 4u;
      v1370 ^= 0x87u;
      v1352 ^= 0x42u;
      v1358 ^= 0x2Du;
      v1355 ^= 0x6Bu;
      v1382 ^= 0xF2u;
      v1377 ^= 0x64u;
      v1372 ^= 0x51u;
      v1364 ^= 0x67u;
      v1365 ^= 0x19u;
      v1390 ^= 0x38u;
      v1379 ^= 0x50u;
      if ( (unsigned int)fksth(&v1350, "BxtlTzUyAjCVoNQOTvYpsWjEgKssLGicffdOfdcPLdtem") )
      {
        printf("OxIdVxjpxTJNqpXITqJ:");
        input_line(&v1916, 0x32uLL);
        v1921 ^= 0xBFu;
        v1949 ^= 0xA5u;
        v1919 ^= 0x19u;
        v1920 ^= 0xBEu;
        v1918 ^= 0xDAu;
        v1939 ^= 0x89u;
        v1948 ^= 0xABu;
        v1961 ^= 0x10u;
        v1926 ^= 0x6Au;
        v1946 ^= 0xEAu;
        v1959 ^= 0xDDu;
        v1962 ^= 0x62u;
        v1929 ^= 0x46u;
        v1932 ^= 0xB8u;
        v1923 ^= 0x7Cu;
        v1927 ^= 0xE6u;
        v1953 ^= 0xB1u;
        v1963 ^= 0x2Du;
        v1957 ^= 0x51u;
        v1925 ^= 0x43u;
        v1941 ^= 0xD2u;
        v1943 ^= 0x5Cu;
        v1916 ^= 0xAEu;
        v1917 ^= 0xFDu;
        v1952 ^= 0x4Eu;
        v1936 ^= 0x65u;
        v1931 ^= 0xD0u;
        v1930 ^= 0xEDu;
        v1951 ^= 0x9Bu;
        v1937 ^= 0xA5u;
        v1935 ^= 0xDu;
        v1944 ^= 0x46u;
        v1954 ^= 0x52u;
        v1934 ^= 0xD0u;
        v1942 ^= 0xC0u;
        v1960 ^= 0xE2u;
        v1924 ^= 0x3Du;
        v1938 ^= 0x51u;
        v1958 ^= 0xDEu;
        v1922 ^= 0x5Cu;
        v1933 ^= 0xE0u;
        v1955 ^= 0x51u;
        v1940 ^= 0xCEu;
        v1928 ^= 0x42u;
        v1945 ^= 0xD7u;
        v1956 ^= 0xEAu;
        v1947 ^= 0x61u;
        v1950 ^= 0xDEu;
        if ( (unsigned int)fksth(&v1916, "kfdzDpYjCrDanPfcnQSvDgwHdvkHWOYtpnoFedNGIRDVekFXuc") )
        {
          printf("fILdiYbgDG:");
          v2984 = input_val();
          v2985 = input_val();
          v2986 = input_val();
          v2987 = input_val();
          v2988 = input_val();
          v2989 = input_val();
          v2990 = input_val();
          if ( v2985 - v2990 == 15303 )
          {
            printf("fLDNbpOcGx:");
            v2979 = input_val();
            v2980 = input_val();
            v2981 = input_val();
            v2982 = input_val();
            v2983 = input_val();
            if ( v2980 - v2982 == 62545 )
            {
              printf("OrVmbGzuPtYhWxtHN:");
              input_line(&v1088, 0x2BuLL);
              v1107 ^= 0x9Au;
              v1111 ^= 0xB6u;
              v1097 ^= 0xB4u;
              v1108 ^= 0xD3u;
              v1090 ^= 0x47u;
              v1129 ^= 0x34u;
              v1094 ^= 0xBAu;
              v1130 ^= 0x5Eu;
              v1101 ^= 0x4Du;
              v1128 ^= 0x80u;
              v1100 ^= 0x65u;
              v1096 ^= 0x58u;
              v1117 ^= 0xF2u;
              v1091 ^= 0x3Eu;
              v1093 ^= 0x89u;
              v1118 ^= 0x92u;
              v1099 ^= 0x41u;
              v1095 ^= 0x9Au;
              v1125 ^= 0xF7u;
              v1106 ^= 0xF9u;
              v1103 ^= 0x8Du;
              v1098 ^= 0x68u;
              v1105 ^= 0x42u;
              v1112 ^= 0xB1u;
              v1102 ^= 0xD5u;
              v1119 ^= 0xE0u;
              v1126 ^= 0x31u;
              v1089 ^= 0x19u;
              v1114 ^= 0x35u;
              v1127 ^= 1u;
              v1122 ^= 0x23u;
              v1121 ^= 2u;
              v1123 ^= 0x40u;
              v1116 ^= 0x89u;
              v1092 ^= 0xA2u;
              v1120 ^= 0xF5u;
              v1113 ^= 0xBDu;
              v1115 ^= 0xFBu;
              v1109 ^= 0x7Cu;
              v1104 ^= 0xD7u;
              v1124 ^= 0x8Cu;
              v1110 ^= 0x49u;
              v1088 ^= 0x2Eu;
              fksth(&v1088, "jKnjaXTXJWAgkpNqdbToErqUEsZgLtMkEeyIoGVLiXY");
              return 0;
            }
            else
            {
              printf("ANbzvXWonxh:");
              input_line(&v2860, 0x3CuLL);
              v2897 ^= 1u;
              v2899 ^= 0x49u;
              v2916 ^= 0x60u;
              v2905 ^= 0x5Cu;
              v2903 ^= 0x37u;
              v2909 ^= 0x7Cu;
              v2875 ^= 0x30u;
              v2877 ^= 0x37u;
              v2893 ^= 0x3Fu;
              v2881 ^= 0xF0u;
              v2878 ^= 6u;
              v2873 ^= 0x15u;
              v2871 ^= 0xCAu;
              v2890 ^= 0xCDu;
              v2917 ^= 0xF0u;
              v2895 ^= 0x7Du;
              v2864 ^= 0xA1u;
              v2868 ^= 0x9Du;
              v2887 ^= 0x56u;
              v2901 ^= 0xBCu;
              v2892 ^= 0xA7u;
              v2863 ^= 0x75u;
              v2904 ^= 0x99u;
              v2883 ^= 0xB8u;
              v2862 ^= 0xB3u;
              v2882 ^= 0xE8u;
              v2865 ^= 0xA0u;
              v2896 ^= 0xF6u;
              v2861 ^= 0x59u;
              v2902 ^= 0xD6u;
              v2889 ^= 0x6Du;
              v2918 ^= 0x5Du;
              v2908 ^= 0xE7u;
              v2872 ^= 0x9Au;
              v2915 ^= 0xAEu;
              v2888 ^= 0x39u;
              v2913 ^= 0x31u;
              v2867 ^= 0xBBu;
              v2910 ^= 0xDFu;
              v2866 ^= 0x75u;
              v2906 ^= 0xCEu;
              v2900 ^= 0xA3u;
              v2907 ^= 0x8Au;
              v2885 ^= 0xB4u;
              v2879 ^= 0x67u;
              v2869 ^= 0x80u;
              v2860 ^= 0xD1u;
              v2911 ^= 0x3Cu;
              v2914 ^= 0x52u;
              v2898 ^= 0x6Fu;
              v2891 ^= 0xCEu;
              v2876 ^= 0xDEu;
              v2884 ^= 0xE8u;
              v2912 ^= 0xEEu;
              v2874 ^= 0xD7u;
              v2870 ^= 0x6Du;
              v2886 ^= 0x2Au;
              v2894 ^= 0x8Fu;
              v2880 ^= 0x8Fu;
              if ( !(unsigned int)fksth(&v2860, "XmbKRdrlwOhqsYGkIFXjKWukNWtnUDRuCVMKInnDDsqnFymarRASiEsCJsdD") )
              {
                printf("tRyPMsjOqo:");
                input_line(&v3381, 0x32uLL);
                v3383 ^= 0xCBu;
                v3386 ^= 0xE6u;
                v3385 ^= 0xD5u;
                v3382 ^= 0x21u;
                v3384 ^= 0x1Au;
                fksth(&v3381, "GybcYZwFN");
              }
              return 0;
            }
          }
          else
          {
            printf("ETirFQcNBk:");
            input_line(&v1531, 0x2EuLL);
            v1563 ^= 0xBBu;
            v1551 ^= 0x4Eu;
            v1543 ^= 0xA4u;
            v1575 ^= 0xC2u;
            v1568 ^= 0x9Au;
            v1548 ^= 0x32u;
            v1552 ^= 0x37u;
            v1561 ^= 0x85u;
            v1553 ^= 0x17u;
            v1539 ^= 0x86u;
            v1565 ^= 0xD1u;
            v1534 ^= 0x8Du;
            v1557 ^= 0xADu;
            v1574 ^= 0xA8u;
            v1572 ^= 0x32u;
            v1532 ^= 0xE9u;
            v1573 ^= 0xCDu;
            v1567 ^= 0x4Du;
            v1566 ^= 0xA2u;
            v1531 ^= 0x98u;
            v1576 ^= 0xFEu;
            v1533 ^= 0xCCu;
            v1569 ^= 0x31u;
            v1536 ^= 0x50u;
            v1571 ^= 0xACu;
            v1535 ^= 0xEDu;
            v1570 ^= 0xFDu;
            v1555 ^= 0xBEu;
            v1549 ^= 0x6Eu;
            v1547 ^= 0x19u;
            v1562 ^= 0xCAu;
            v1554 ^= 0x5Eu;
            v1541 ^= 0x41u;
            v1556 ^= 0xBAu;
            v1559 ^= 0xE4u;
            v1538 ^= 0x84u;
            v1550 ^= 0x89u;
            v1560 ^= 0x6Au;
            v1564 ^= 0xAFu;
            v1537 ^= 0x24u;
            v1540 ^= 0x79u;
            v1544 ^= 0x2Cu;
            v1545 ^= 0x6Cu;
            v1542 ^= 0x3Cu;
            v1546 ^= 0x9Bu;
            v1558 ^= 0x67u;
            if ( (unsigned int)fksth(&v1531, "skCdvmznqInKaVvjblQYBXXWiEhWncgbJzJLlxEpLJYyia") )
            {
              printf("HXOYGGqbZMtT:");
              input_line(&v2919, 0x3CuLL);
              v2971 ^= 0xA8u;
              v2952 ^= 3u;
              v2962 ^= 9u;
              v2975 ^= 0xCFu;
              v2924 ^= 0xB9u;
              v2950 ^= 0xB0u;
              v2941 ^= 0x50u;
              v2939 ^= 0x8Eu;
              v2978 ^= 0x77u;
              v2968 ^= 0xE7u;
              v2945 ^= 0x12u;
              v2977 ^= 0xA2u;
              v2938 ^= 0xFEu;
              v2942 ^= 0x23u;
              v2953 ^= 0x5Eu;
              v2922 ^= 0x80u;
              v2932 ^= 0x76u;
              v2949 ^= 0xE7u;
              v2956 ^= 0xC5u;
              v2947 ^= 0x91u;
              v2926 ^= 0x76u;
              v2935 ^= 0xEEu;
              v2955 ^= 0x95u;
              v2970 ^= 0x2Au;
              v2974 ^= 0xC5u;
              v2931 ^= 0x37u;
              v2928 ^= 0x5Cu;
              v2921 ^= 0x2Du;
              v2944 ^= 0x63u;
              v2940 ^= 0x40u;
              v2969 ^= 0x77u;
              v2946 ^= 0x79u;
              v2936 ^= 0xE5u;
              v2951 ^= 0x60u;
              v2920 ^= 0x40u;
              v2959 ^= 0x87u;
              v2965 ^= 0x62u;
              v2972 ^= 0x7Eu;
              v2964 ^= 0x7Au;
              v2976 ^= 0x56u;
              v2963 ^= 0x69u;
              v2961 ^= 0x7Cu;
              v2925 ^= 0x26u;
              v2966 ^= 0x7Cu;
              v2954 ^= 0x88u;
              v2930 ^= 0x23u;
              v2943 ^= 0x6Au;
              v2957 ^= 0xECu;
              v2923 ^= 0x97u;
              v2919 ^= 0xC3u;
              v2933 ^= 0x55u;
              v2960 ^= 0xBCu;
              v2927 ^= 0xA0u;
              v2967 ^= 0x46u;
              v2934 ^= 0x83u;
              v2948 ^= 0xAFu;
              v2973 ^= 0x62u;
              v2958 ^= 0xAFu;
              v2937 ^= 0xF8u;
              v2929 ^= 0xF3u;
              fksth(&v2919, "jfdQjKTJkwyIVZlZQNijvEDHyMgGgtRhzdlySAcRWJykIXBgwNfVRKKaHitX");
            }
            else
            {
              printf("nyLPvTuTlK:");
              v124 = input_val();
              v125 = input_val();
              v126 = input_val();
              v127 = input_val();
              v128 = input_val();
              v129 = input_val();
              v130 = input_val();
              v131 = input_val();
            }
            return 0;
          }
        }
        else
        {
          printf("ogIWaZyzZixFjYKsp:");
          input_line(v765, 0x27uLL);
          v768 ^= 0xD6u;
          v779 ^= 0xA7u;
          v769 ^= 0xAFu;
          v765[3] ^= 0x84u;
          v794 ^= 0x97u;
          v776 ^= 0xA2u;
          v774 ^= 0x64u;
          v765[2] ^= 0x7Cu;
          v765[4] ^= 0x31u;
          v780 ^= 0xEDu;
          v765[6] ^= 0xA4u;
          v778 ^= 0x35u;
          v791 ^= 0xBFu;
          v765[1] ^= 0xB0u;
          v766 ^= 0x88u;
          v765[5] ^= 0x64u;
          v770 ^= 0x8Bu;
          v793 ^= 0xE5u;
          v773 ^= 0x46u;
          v789 ^= 0x3Cu;
          v782 ^= 0x74u;
          v783 ^= 0xC9u;
          v777 ^= 0x1Eu;
          v787 ^= 0x2Du;
          v790 ^= 0x8Cu;
          v781 ^= 0xA3u;
          v786 ^= 0xC4u;
          v772 ^= 0x2Du;
          v795 ^= 0xA8u;
          v785 ^= 0x57u;
          v765[7] ^= 0xB6u;
          v771 ^= 0xE6u;
          v765[0] ^= 0xD8u;
          v775 ^= 0xB5u;
          v792 ^= 0xADu;
          v788 ^= 0x38u;
          v767 ^= 0x22u;
          v784 ^= 0x57u;
          if ( (unsigned int)fksth(v765, "MXHnlqstZQsFdKkrkJXKCCsLWiNKanUNfnbGGiY") )
          {
            printf("hiOOJVHXOk:");
            v2991 = input_val();
            v2992 = input_val();
            v2993 = input_val();
            v2994 = input_val();
            v2995 = input_val();
            v2996 = input_val();
            if ( ((v2993 + v2995) ^ v2992) == 48382 )
            {
              printf("qrTXSFNhWGwypUl:");
              input_line(&v2800, 0x3CuLL);
              v2839 ^= 0x55u;
              v2804 ^= 0x82u;
              v2813 ^= 0xC8u;
              v2833 ^= 0x3Eu;
              v2812 ^= 0xDEu;
              v2858 ^= 0x86u;
              v2817 ^= 0x32u;
              v2849 ^= 0xE6u;
              v2829 ^= 0x58u;
              v2818 ^= 0xF9u;
              v2819 ^= 0x83u;
              v2854 ^= 0xAu;
              v2814 ^= 0x32u;
              v2848 ^= 0x8Eu;
              v2816 ^= 0x71u;
              v2845 ^= 0xEFu;
              v2837 ^= 0xC0u;
              v2825 ^= 0x52u;
              v2842 ^= 0x80u;
              v2844 ^= 0xAAu;
              v2853 ^= 0x3Bu;
              v2836 ^= 0xE0u;
              v2805 ^= 0x9Bu;
              v2826 ^= 0x37u;
              v2800 ^= 0xA9u;
              v2831 ^= 0xF4u;
              v2830 ^= 0x50u;
              v2859 ^= 0xDCu;
              v2851 ^= 0xCCu;
              v2850 ^= 0xA6u;
              v2821 ^= 0x77u;
              v2834 ^= 0xB1u;
              v2809 ^= 0x91u;
              v2841 ^= 0x84u;
              v2828 ^= 0x18u;
              v2855 ^= 0x85u;
              v2806 ^= 0x26u;
              v2846 ^= 0x4Au;
              v2820 ^= 0xFDu;
              v2815 ^= 0xA2u;
              v2811 ^= 0xAu;
              v2843 ^= 0x2Du;
              v2857 ^= 0x3Du;
              v2802 ^= 0x6Fu;
              v2840 ^= 0xC8u;
              v2808 ^= 0x5Du;
              v2835 ^= 0xF7u;
              v2807 ^= 0xD7u;
              v2810 ^= 0x83u;
              v2803 ^= 0x1Bu;
              v2852 ^= 0xADu;
              v2824 ^= 0xE6u;
              v2801 ^= 0x4Du;
              v2827 ^= 0x5Au;
              v2838 ^= 0xC7u;
              v2856 ^= 0xEDu;
              v2847 ^= 7u;
              v2822 ^= 0x4Du;
              v2832 ^= 0x93u;
              v2823 ^= 0x9Eu;
              fksth(&v2800, "VHoNlprXsPIJEGexCePhiEhrNmMqGfdmKQHqHzxjfQpOwpovSNeixTIIbAwH");
            }
            else
            {
              printf("TnDklKcgEfXXbhA:");
              input_line(&v1624, 0x2FuLL);
              v1648 ^= 0x98u;
              v1666 ^= 0x3Eu;
              v1663 ^= 0xE4u;
              v1632 ^= 0x8Du;
              v1643 ^= 0x4Cu;
              v1645 ^= 0xFAu;
              v1638 ^= 0x99u;
              v1631 ^= 0xA6u;
              v1661 ^= 0xABu;
              v1646 ^= 0xD3u;
              v1630 ^= 0x66u;
              v1639 ^= 0x8Eu;
              v1658 ^= 0x17u;
              v1627 ^= 0x4Au;
              v1629 ^= 0x9Eu;
              v1642 ^= 0x92u;
              v1664 ^= 0x93u;
              v1649 ^= 5u;
              v1659 ^= 0xCAu;
              v1667 ^= 0x5Bu;
              v1670 ^= 0x1Fu;
              v1652 ^= 0x3Du;
              v1633 ^= 0x4Eu;
              v1636 ^= 0xFDu;
              v1624 ^= 0x90u;
              v1650 ^= 0x75u;
              v1653 ^= 0x2Au;
              v1669 ^= 0x6Eu;
              v1644 ^= 0x6Eu;
              v1634 ^= 0x76u;
              v1654 ^= 0x15u;
              v1656 ^= 0xB8u;
              v1660 ^= 0x74u;
              v1628 ^= 0x51u;
              v1665 ^= 0xC9u;
              v1625 ^= 0x74u;
              v1655 ^= 0x73u;
              v1657 ^= 0x69u;
              v1626 ^= 0x47u;
              v1668 ^= 0xD9u;
              v1662 ^= 0x69u;
              v1651 ^= 0x63u;
              v1647 ^= 0xEEu;
              v1635 ^= 0x2Eu;
              v1637 ^= 0x74u;
              v1640 ^= 0x25u;
              v1641 ^= 0x17u;
              fksth(&v1624, "XUsNznevnpeDXWoMhmZiwGmGtNVWSlOTGbBCvihGMKNfhRN");
            }
            return 0;
          }
          else
          {
            printf("iVokddpuqeQ:");
            input_line(&v578, 0x24uLL);
            v588 ^= 0xEAu;
            v581 ^= 0x51u;
            v583 ^= 0xE1u;
            v601 ^= 0x4Fu;
            v602 ^= 0xE5u;
            v595 ^= 0x9Cu;
            v612 ^= 0x73u;
            v606 ^= 0x4Cu;
            v587 ^= 0xE1u;
            v578 ^= 0x79u;
            v582 ^= 0xDu;
            v599 ^= 0xEEu;
            v597 ^= 0x8Eu;
            v598 ^= 0x46u;
            v589 ^= 0xA0u;
            v605 ^= 0xA0u;
            v593 ^= 0x68u;
            v611 ^= 0x6Du;
            v613 ^= 0x21u;
            v594 ^= 0xB7u;
            v607 ^= 0x47u;
            v603 ^= 0xEEu;
            v590 ^= 0x13u;
            v600 ^= 0x22u;
            v580 ^= 0xE5u;
            v609 ^= 0x1Eu;
            v591 ^= 0xFEu;
            v592 ^= 0x28u;
            v585 ^= 0x95u;
            v604 ^= 0x54u;
            v610 ^= 0x9Fu;
            v596 ^= 0xE9u;
            v584 ^= 0x3Au;
            v608 ^= 6u;
            v586 ^= 0x72u;
            v579 ^= 0x37u;
            if ( (unsigned int)fksth(&v578, "nbUtlcEniyKZyeCPzBufRyNAvTmKkaPhlIlI") )
            {
              printf("JFVyQKfxByrxEIadVk:");
              input_line(&v651, 0x25uLL);
              v668 ^= 0xF5u;
              v665 ^= 0x3Eu;
              v680 ^= 0x4Du;
              v666 ^= 0x21u;
              v675 ^= 0x28u;
              v686 ^= 0xFEu;
              v672 ^= 0x14u;
              v684 ^= 0x62u;
              v679 ^= 0x4Fu;
              v652 ^= 0x2Cu;
              v685 ^= 0xFu;
              v676 ^= 0xBBu;
              v658 ^= 0x15u;
              v663 ^= 0xE0u;
              v681 ^= 0xD5u;
              v678 ^= 0xCu;
              v659 ^= 0x8Fu;
              v660 ^= 0x78u;
              v655 ^= 0x13u;
              v671 ^= 0xE9u;
              v683 ^= 0x6Du;
              v653 ^= 0x16u;
              v664 = ~v664;
              v657 ^= 0xD3u;
              v674 ^= 0x24u;
              v651 = ~v651;
              v682 ^= 2u;
              v670 ^= 0x96u;
              v656 ^= 0x81u;
              v662 ^= 0x3Cu;
              v677 ^= 0x64u;
              v669 ^= 0xEDu;
              v654 ^= 0x78u;
              v661 ^= 0x93u;
              v667 ^= 0x31u;
              v687 ^= 0x53u;
              v673 ^= 8u;
              fksth(&v651, "DRlWyxbSuuIeTUKOZxCKisjDpqjfPakbXyPgD");
            }
            else
            {
              printf("HVcqQkdAvP:");
              v2997 = input_val();
              v2998 = input_val();
              v2999 = input_val();
              v3000 = input_val();
              v3001 = input_val();
              v3002 = input_val();
              v3003 = input_val();
            }
            return 0;
          }
        }
      }
      else
      {
        printf("XvIYSyCWqukEbYkS:");
        input_line(&v2224, 0x37uLL);
        v2247 ^= 0xDFu;
        v2273 ^= 0xB7u;
        v2253 ^= 0x96u;
        v2271 ^= 0xBEu;
        v2258 ^= 6u;
        v2238 ^= 0x5Du;
        v2231 ^= 0xBEu;
        v2270 ^= 0x17u;
        v2274 ^= 0xE5u;
        v2245 ^= 0x98u;
        v2266 ^= 0x7Bu;
        v2248 ^= 0xC5u;
        v2237 ^= 0xB6u;
        v2256 ^= 0x13u;
        v2246 ^= 8u;
        v2263 ^= 0x35u;
        v2278 ^= 0x47u;
        v2257 ^= 0xD6u;
        v2233 ^= 0x38u;
        v2252 ^= 2u;
        v2265 ^= 0x1Bu;
        v2234 ^= 0xFBu;
        v2226 ^= 0xFCu;
        v2260 ^= 0xE0u;
        v2249 ^= 0x7Au;
        v2232 ^= 0x3Fu;
        v2225 ^= 0x90u;
        v2272 ^= 0xF0u;
        v2268 ^= 0xDFu;
        v2227 ^= 0xDCu;
        v2250 ^= 0x6Bu;
        v2235 ^= 0x9Au;
        v2244 ^= 0x3Fu;
        v2269 ^= 0x1Cu;
        v2242 ^= 0x5Au;
        v2275 ^= 0x79u;
        v2251 ^= 0xEDu;
        v2240 ^= 0x82u;
        v2241 ^= 0x9Cu;
        v2224 ^= 0x34u;
        v2243 ^= 0xC2u;
        v2254 ^= 0xE7u;
        v2262 ^= 0x64u;
        v2267 ^= 0x9Du;
        v2229 ^= 0x55u;
        v2277 ^= 0x84u;
        v2255 ^= 0xEDu;
        v2276 = ~v2276;
        v2261 ^= 0x2Cu;
        v2239 ^= 0x4Eu;
        v2264 ^= 6u;
        v2236 ^= 0x72u;
        v2228 ^= 0x6Bu;
        v2230 ^= 0x4Du;
        v2259 ^= 0x34u;
        if ( (unsigned int)fksth(&v2224, "zyYpnxjqXyUnvBTmpQMRtbaYjwhvIZjcCFdozJLuUQIxPjhBTifMuUQ") )
        {
          printf("IJnabKHYog:");
          v3025 = input_val();
          v3026 = input_val();
          v3027 = input_val();
          v3028 = input_val();
          if ( (v3025 ^ v3027) == 53715 )
          {
            printf("xVpCpxniAv:");
            input_line(&v1261, 0x2CuLL);
            v1293 ^= 0xA4u;
            v1269 ^= 0xBAu;
            v1272 ^= 0x56u;
            v1288 ^= 0x79u;
            v1299 ^= 3u;
            v1279 ^= 0xECu;
            v1301 ^= 0x39u;
            v1265 ^= 0x15u;
            v1271 ^= 0xDu;
            v1264 ^= 0x74u;
            v1284 ^= 0xA7u;
            v1261 ^= 0x11u;
            v1268 ^= 6u;
            v1295 ^= 0x6Bu;
            v1270 ^= 0x7Au;
            v1287 ^= 0x10u;
            v1263 ^= 0x75u;
            v1289 ^= 0x16u;
            v1267 ^= 0x80u;
            v1274 ^= 0xC2u;
            v1304 ^= 0xE6u;
            v1275 = ~v1275;
            v1300 ^= 0x6Cu;
            v1262 ^= 0x4Au;
            v1283 ^= 0x7Du;
            v1296 ^= 0x22u;
            v1291 ^= 0xF6u;
            v1294 ^= 0x88u;
            v1290 ^= 0xCAu;
            v1302 ^= 0xF4u;
            v1285 ^= 0x53u;
            v1266 ^= 0xCBu;
            v1281 ^= 0x29u;
            v1280 ^= 0x72u;
            v1286 ^= 0x93u;
            v1276 ^= 0x31u;
            v1297 ^= 0x98u;
            v1277 ^= 0xB5u;
            v1303 ^= 0x37u;
            v1273 ^= 0x26u;
            v1282 ^= 0x5Du;
            v1278 ^= 0x82u;
            v1292 ^= 0x15u;
            v1298 ^= 0xA8u;
            if ( (unsigned int)fksth(&v1261, "WdRrMztycWpsUZnYvkuTsUmJovrRLLyNkVrOTRJHNqsV") )
            {
              printf("nrEfNTTLEwYxQ:");
              input_line(&v1394, 0x2DuLL);
              v1435 ^= 0x26u;
              v1425 ^= 0x68u;
              v1403 ^= 0x52u;
              v1414 ^= 0x6Au;
              v1402 ^= 0xACu;
              v1434 ^= 0x95u;
              v1395 ^= 0xFCu;
              v1436 ^= 0xEFu;
              v1399 ^= 0xC1u;
              v1426 ^= 0x51u;
              v1408 ^= 0x1Au;
              v1413 ^= 0xB3u;
              v1410 ^= 0x70u;
              v1409 ^= 0xC4u;
              v1407 ^= 0xE0u;
              v1401 ^= 0xBAu;
              v1397 ^= 0x98u;
              v1406 ^= 0x45u;
              v1437 ^= 0x49u;
              v1411 ^= 0xB0u;
              v1429 ^= 0x80u;
              v1438 ^= 0xA6u;
              v1394 ^= 0x94u;
              v1398 ^= 0x9Au;
              v1418 ^= 0xF3u;
              v1430 ^= 0xE6u;
              v1421 ^= 0x37u;
              v1404 ^= 0xE9u;
              v1417 ^= 0x74u;
              v1427 ^= 0xF6u;
              v1412 ^= 0x27u;
              v1420 ^= 0x40u;
              v1396 ^= 0xE1u;
              v1433 ^= 0x23u;
              v1405 ^= 0xC2u;
              v1400 ^= 0xAEu;
              v1416 ^= 0xCCu;
              v1424 ^= 0x79u;
              v1428 ^= 0x53u;
              v1423 ^= 0xB5u;
              v1431 ^= 0xA0u;
              v1422 ^= 9u;
              v1419 ^= 0x50u;
              v1432 ^= 0x3Eu;
              v1415 ^= 0xEAu;
              fksth(&v1394, "eaZrbCdoVyHavDaJgaMiqdsSYIiPxdnxCsgtuUiSPKliL");
            }
            else
            {
              printf("gysjnkUjSq:");
              v3018 = input_val();
              v3019 = input_val();
              v3020 = input_val();
              v3021 = input_val();
              v3022 = input_val();
              v3023 = input_val();
              v3024 = input_val();
            }
            return 0;
          }
          else
          {
            printf("qbFpflLXha:");
            v3011 = input_val();
            v3012 = input_val();
            v3013 = input_val();
            v3014 = input_val();
            v3015 = input_val();
            v3016 = input_val();
            v3017 = input_val();
            if ( (v3014 ^ v3012 ^ v3015) == 43239 )
            {
              printf("WWPsDTLiXn:");
              v3004 = input_val();
              v3005 = input_val();
              v3006 = input_val();
              v3007 = input_val();
              v3008 = input_val();
              v3009 = input_val();
              v3010 = input_val();
            }
            else
            {
              printf("mrhQQpHtmy:");
              v116 = input_val();
              v117 = input_val();
              v118 = input_val();
              v119 = input_val();
              v120 = input_val();
              v121 = input_val();
              v122 = input_val();
              v123 = input_val();
            }
            return 0;
          }
        }
        else
        {
          printf("NfZWiYbaSc:");
          v3038 = input_val();
          v3039 = input_val();
          v3040 = input_val();
          v3041 = input_val();
          v3042 = input_val();
          if ( v3039 * v3038 * v3042 == 15103 )
          {
            printf("sztIqcRqRj:");
            v3034 = input_val();
            v3035 = input_val();
            v3036 = input_val();
            v3037 = input_val();
            if ( (v3035 ^ (v3036 * v3037)) == 11891 )
            {
              printf("qCFMfGvChbNrdliHUVj:");
              input_line(&v2335, 0x38uLL);
              v2381 ^= 0xB4u;
              v2350 ^= 0x83u;
              v2348 ^= 0xC3u;
              v2357 ^= 0xB6u;
              v2378 ^= 0x38u;
              v2369 ^= 0x97u;
              v2377 ^= 0xB2u;
              v2387 ^= 0xD8u;
              v2384 ^= 0x80u;
              v2346 ^= 0xB8u;
              v2372 ^= 0xBCu;
              v2340 ^= 0x38u;
              v2341 ^= 0x8Cu;
              v2349 ^= 0xFDu;
              v2336 ^= 0x19u;
              v2354 ^= 0xBFu;
              v2345 ^= 0x4Du;
              v2371 ^= 0xA7u;
              v2335 ^= 0xEDu;
              v2379 ^= 0xAAu;
              v2382 ^= 0x6Bu;
              v2388 ^= 0xB8u;
              v2359 ^= 0x6Au;
              v2337 ^= 0x3Fu;
              v2358 ^= 0x91u;
              v2342 ^= 0x62u;
              v2380 ^= 0x6Du;
              v2390 ^= 0xC2u;
              v2360 ^= 0xAEu;
              v2367 ^= 0x2Au;
              v2361 ^= 0xF0u;
              v2356 ^= 0x43u;
              v2383 ^= 0x17u;
              v2343 ^= 0xEBu;
              v2365 ^= 0xA4u;
              v2344 ^= 0xBu;
              v2385 ^= 0x85u;
              v2366 ^= 0x98u;
              v2370 ^= 0xABu;
              v2338 ^= 0x4Du;
              v2376 ^= 0x71u;
              v2355 ^= 0x4Fu;
              v2375 ^= 0x5Eu;
              v2352 ^= 0x6Cu;
              v2386 ^= 0x35u;
              v2368 ^= 0xEEu;
              v2353 ^= 0xEu;
              v2362 ^= 0x89u;
              v2339 ^= 0xF0u;
              v2389 ^= 0xD7u;
              v2364 ^= 0x11u;
              v2347 ^= 0x71u;
              v2374 ^= 0x54u;
              v2351 ^= 0xD0u;
              v2363 ^= 0x3Bu;
              v2373 ^= 0x57u;
              fksth(&v2335, "owxUfjSUpFmMwNBnySMfAsDyuVbubwQMyYqhZJbWJTPYcvTTuvDeNMvf");
            }
            else
            {
              printf("CpqnPTMoAaKWGy:");
              input_line(&v198, 0x21uLL);
              v211 ^= 0xF4u;
              v209 ^= 0xF5u;
              v225 ^= 0x61u;
              v199 ^= 0x63u;
              v230 ^= 0xE4u;
              v215 ^= 0x6Cu;
              v210 ^= 0x7Eu;
              v208 ^= 0x55u;
              v220 ^= 0xCFu;
              v204 ^= 0x8Bu;
              v214 ^= 0x2Du;
              v219 ^= 2u;
              v202 ^= 0x21u;
              v222 ^= 0x8Cu;
              v216 ^= 0x9Cu;
              v218 ^= 0x31u;
              v207 ^= 0x6Du;
              v198 ^= 0x61u;
              v226 ^= 0x66u;
              v205 ^= 0x4Au;
              v206 ^= 0x6Du;
              v223 ^= 0xCDu;
              v213 ^= 0x25u;
              v229 ^= 0xB6u;
              v203 ^= 0xCEu;
              v224 ^= 0x1Au;
              v227 ^= 0xA6u;
              v221 ^= 0x8Cu;
              v217 ^= 0xC7u;
              v201 ^= 0x44u;
              v212 ^= 0x8Cu;
              v200 ^= 0xACu;
              v228 ^= 0x19u;
              fksth(&v198, "ErrPAdAyGzwyNdKvVbiirDECEBIIYbltr");
            }
            return 0;
          }
          else
          {
            printf("IBqIMvoXce:");
            v3029 = input_val();
            v3030 = input_val();
            v3031 = input_val();
            v3032 = input_val();
            v3033 = input_val();
            if ( ((v3030 - v3031) ^ v3032) == 951 )
            {
              printf("ObIWMQgrxRLymyCDQ:");
              input_line(&v2391, 0x39uLL);
              v2439 ^= 0x60u;
              v2440 ^= 0x6Fu;
              v2442 ^= 0x6Eu;
              v2398 ^= 9u;
              v2431 ^= 0xAu;
              v2394 ^= 0x72u;
              v2400 ^= 0x92u;
              v2435 ^= 0x99u;
              v2433 ^= 0xB5u;
              v2424 ^= 0xCBu;
              v2410 ^= 0xA1u;
              v2401 ^= 0x7Eu;
              v2438 ^= 0x18u;
              v2406 ^= 0xAEu;
              v2412 ^= 0x7Bu;
              v2441 ^= 0xDDu;
              v2416 ^= 0x26u;
              v2399 ^= 0x34u;
              v2443 ^= 0x84u;
              v2391 ^= 0xF5u;
              v2409 ^= 0xCDu;
              v2396 ^= 0xE4u;
              v2423 ^= 0x3Au;
              v2395 ^= 0x9Bu;
              v2418 ^= 0xC8u;
              v2436 ^= 0xAAu;
              v2445 ^= 0x59u;
              v2421 ^= 2u;
              v2408 ^= 0xA5u;
              v2407 ^= 0xF6u;
              v2444 ^= 0x42u;
              v2411 ^= 0xBEu;
              v2425 ^= 0x73u;
              v2420 ^= 0xCAu;
              v2437 ^= 0x2Bu;
              v2446 ^= 0x18u;
              v2429 ^= 0xBEu;
              v2404 ^= 0x1Cu;
              v2432 ^= 0x97u;
              v2422 ^= 0xAAu;
              v2434 ^= 0x56u;
              v2402 ^= 0xAAu;
              v2393 ^= 0xAu;
              v2397 ^= 0x47u;
              v2413 ^= 0x17u;
              v2405 ^= 0x9Fu;
              v2428 ^= 0xDCu;
              v2392 ^= 0x2Fu;
              v2415 ^= 0x61u;
              v2430 ^= 0x4Eu;
              v2403 ^= 0xF5u;
              v2447 ^= 0x6Eu;
              v2414 ^= 0x1Bu;
              v2427 ^= 0x1Du;
              v2417 ^= 4u;
              v2426 ^= 0x80u;
              v2419 ^= 0x5Au;
              fksth(&v2391, "tSKEyZszofTzfODKhdwvKnfqOXGOkrzJqnZUxDfPoGWHXzREJsRUvuwBj");
            }
            else
            {
              printf("RUxARWOYbnoK:");
              input_line(&v367, 0x22uLL);
              v389 ^= 0xE4u;
              v378 ^= 0x43u;
              v368 ^= 0xB7u;
              v395 ^= 0x79u;
              v373 ^= 0x2Eu;
              v390 ^= 0xE0u;
              v393 ^= 0xBBu;
              v372 ^= 0x13u;
              v392 ^= 0xD9u;
              v388 ^= 0xD8u;
              v398 ^= 0x7Bu;
              v375 ^= 0x73u;
              v380 ^= 0x76u;
              v384 ^= 0xEAu;
              v383 ^= 0x45u;
              v379 ^= 0xBBu;
              v400 ^= 0x66u;
              v369 ^= 6u;
              v399 ^= 0x19u;
              v382 ^= 0xFu;
              v391 ^= 0x4Du;
              v377 ^= 5u;
              v397 ^= 0x2Eu;
              v394 ^= 0x4Du;
              v396 ^= 0x49u;
              v385 ^= 0x42u;
              v374 ^= 0xB6u;
              v370 ^= 0x43u;
              v367 ^= 0x4Bu;
              v381 ^= 0xBu;
              v387 ^= 0xA3u;
              v371 ^= 0x9Eu;
              v376 ^= 0xA6u;
              v386 ^= 0xB8u;
              fksth(&v367, "NNnYUIfcGgCZOqaxCtimTdCvumNqfGPYSf");
            }
            return 0;
          }
        }
      }
    }
    else
    {
      printf("HundNZANbe:");
      v3123 = input_val();
      v3124 = input_val();
      v3125 = input_val();
      v3126 = input_val();
      v3127 = input_val();
      if ( (v3124 ^ v3127) == 16935 )
      {
        printf("dpNebsYWgas:");
        input_line(&v960, 0x2AuLL);
        v969 ^= 0xE7u;
        v995 ^= 0x71u;
        v992 ^= 0xA7u;
        v963 ^= 0x78u;
        v996 ^= 0xB2u;
        v981 ^= 0xF4u;
        v990 ^= 0x7Du;
        v984 ^= 0xA0u;
        v962 ^= 0xE5u;
        v983 ^= 0x27u;
        v972 ^= 0x17u;
        v999 ^= 0x70u;
        v974 ^= 0x92u;
        v967 ^= 8u;
        v960 ^= 0x67u;
        v966 ^= 0xFAu;
        v982 ^= 0xD1u;
        v976 ^= 0x20u;
        v994 ^= 0x29u;
        v977 ^= 0x19u;
        v964 ^= 0x3Fu;
        v970 ^= 0xB4u;
        v980 ^= 0xD9u;
        v979 ^= 0xBAu;
        v988 ^= 0x6Du;
        v987 ^= 0xE9u;
        v991 ^= 0xF8u;
        v1000 ^= 0x6Bu;
        v1001 ^= 0xCEu;
        v978 ^= 0x69u;
        v975 ^= 0xDBu;
        v985 ^= 0x7Cu;
        v997 ^= 0xA5u;
        v993 ^= 0xA4u;
        v961 ^= 0x9Fu;
        v971 ^= 0xF1u;
        v973 ^= 0x91u;
        v998 ^= 0xD5u;
        v965 ^= 0x39u;
        v989 ^= 6u;
        v968 ^= 0x7Du;
        v986 ^= 0xD8u;
        if ( (unsigned int)fksth(&v960, "OoPBungeZveVnXuYuGCnihEVflRqHGekeDuMISFAuy") )
        {
          printf("kOBNlzHYdD:");
          v3094 = input_val();
          v3095 = input_val();
          v3096 = input_val();
          v3097 = input_val();
          v3098 = input_val();
          if ( v3094 + v3098 == 31812 )
          {
            printf("aqxafndVHg:");
            v3088 = input_val();
            v3089 = input_val();
            v3090 = input_val();
            v3091 = input_val();
            v3092 = input_val();
            v3093 = input_val();
            if ( v3092 + v3091 + v3093 == 18912 )
            {
              printf("kYnwLvhyyk:");
              v100 = input_val();
              v101 = input_val();
              v102 = input_val();
              v103 = input_val();
              v104 = input_val();
              v105 = input_val();
              v106 = input_val();
              v107 = input_val();
            }
            else
            {
              printf("NajXRSqpik:");
              v3083 = input_val();
              v3084 = input_val();
              v3085 = input_val();
              v3086 = input_val();
              v3087 = input_val();
            }
            return 0;
          }
          else
          {
            printf("lvueHARBNG:");
            v3076 = input_val();
            v3077 = input_val();
            v3078 = input_val();
            v3079 = input_val();
            v3080 = input_val();
            v3081 = input_val();
            v3082 = input_val();
            if ( (v3077 ^ v3079) == 2574 )
            {
              printf("nmYbOOKkif:");
              v108 = input_val();
              v109 = input_val();
              v110 = input_val();
              v111 = input_val();
              v112 = input_val();
              v113 = input_val();
              v114 = input_val();
              v115 = input_val();
            }
            else
            {
              printf("kwiqthzPQu:");
              input_line(&v1719, 0x31uLL);
              v1729 ^= 0x29u;
              v1719 ^= 0xA7u;
              v1721 ^= 0x93u;
              v1723 ^= 0xEFu;
              v1725 ^= 0x5Du;
              v1745 ^= 0xEAu;
              v1757 ^= 0xDFu;
              v1743 ^= 0xA5u;
              v1747 ^= 0xE2u;
              v1748 ^= 0x8Eu;
              v1741 ^= 0xF0u;
              v1739 ^= 0xB5u;
              v1766 ^= 0x18u;
              v1760 ^= 0x6Du;
              v1765 ^= 0x16u;
              v1752 ^= 0xCEu;
              v1762 ^= 0x3Eu;
              v1728 ^= 0xF7u;
              v1753 ^= 0xE5u;
              v1735 ^= 0x75u;
              v1754 ^= 0x78u;
              v1738 ^= 0x85u;
              v1756 ^= 0x60u;
              v1755 ^= 0xBEu;
              v1740 ^= 0x63u;
              v1764 ^= 0xE7u;
              v1749 ^= 0x37u;
              v1724 ^= 6u;
              v1722 ^= 0xB8u;
              v1734 ^= 0x3Bu;
              v1758 ^= 0xE5u;
              v1750 ^= 2u;
              v1727 ^= 0x8Du;
              v1767 ^= 0x39u;
              v1730 ^= 0x21u;
              v1742 ^= 0x10u;
              v1737 ^= 0xD8u;
              v1751 ^= 0xDAu;
              v1759 ^= 0xA5u;
              v1733 ^= 0xCDu;
              v1744 ^= 0x4Bu;
              v1731 ^= 0xF3u;
              v1720 ^= 4u;
              v1761 ^= 0xB0u;
              v1726 ^= 0x3Au;
              v1732 ^= 0xB2u;
              v1763 ^= 0x75u;
              v1736 ^= 0xB7u;
              v1746 ^= 0x35u;
              fksth(&v1719, "GzQWpTMaTxEDyXamjdEmnyuYtJodjuaUiWzKACpkDNtvXYYwQ");
            }
            return 0;
          }
        }
        else
        {
          printf("htAEHObrNL:");
          v3118 = input_val();
          v3119 = input_val();
          v3120 = input_val();
          v3121 = input_val();
          v3122 = input_val();
          if ( v3118 + v3122 == 50052 )
          {
            printf("dDzVlYdZLkYhA:");
            input_line(&v265, 0x22uLL);
            v280 ^= 0xC2u;
            v268 ^= 0x51u;
            v269 ^= 0xD0u;
            v290 ^= 0x78u;
            v291 ^= 0x98u;
            v284 ^= 0x83u;
            v292 ^= 0xDBu;
            v288 ^= 0x6Au;
            v275 ^= 0x2Fu;
            v295 ^= 0x5Cu;
            v294 ^= 0x91u;
            v287 ^= 0x1Au;
            v266 ^= 0xFEu;
            v297 ^= 0x83u;
            v296 ^= 0x28u;
            v283 ^= 0xE8u;
            v286 ^= 0xD3u;
            v277 ^= 0x22u;
            v279 ^= 0xAAu;
            v278 ^= 0xD2u;
            v285 ^= 0xBDu;
            v270 ^= 0xADu;
            v293 ^= 0xC8u;
            v265 ^= 0x4Fu;
            v298 ^= 0xDCu;
            v267 ^= 0x4Eu;
            v289 ^= 0xD8u;
            v276 ^= 0x79u;
            v274 ^= 0xAFu;
            v272 ^= 0x88u;
            v273 ^= 0xE7u;
            v282 ^= 0xD4u;
            v281 ^= 0x4Bu;
            v271 ^= 0x34u;
            if ( (unsigned int)fksth(&v265, "nbzdIkwMmZgYDxiuFQziKiOLzkCarwmGtR") )
            {
              printf("BxrnxQGSIq:");
              v3113 = input_val();
              v3114 = input_val();
              v3115 = input_val();
              v3116 = input_val();
              v3117 = input_val();
            }
            else
            {
              printf("YFTEYPyofY:");
              v92 = input_val();
              v93 = input_val();
              v94 = input_val();
              v95 = input_val();
              v96 = input_val();
              v97 = input_val();
              v98 = input_val();
              v99 = input_val();
            }
            return 0;
          }
          else
          {
            printf("AvfMzPZvDBXMG:");
            input_line(&v726, 0x27uLL);
            v762 ^= 0x15u;
            v726 ^= 0xA5u;
            v742 ^= 0xCCu;
            v745 ^= 0x4Fu;
            v750 ^= 0x4Bu;
            v755 ^= 0x9Bu;
            v749 ^= 0x43u;
            v758 ^= 0x1Au;
            v731 ^= 0xD1u;
            v764 ^= 0x4Au;
            v728 ^= 0xFu;
            v727 ^= 0x93u;
            v741 ^= 0x6Fu;
            v739 ^= 0xF5u;
            v737 ^= 0x4Du;
            v730 ^= 0x45u;
            v740 ^= 0x84u;
            v729 ^= 0x7Cu;
            v733 ^= 9u;
            v759 ^= 0x10u;
            v732 ^= 0xA2u;
            v744 ^= 0xC2u;
            v746 ^= 0xA4u;
            v743 ^= 0x4Du;
            v751 ^= 0x75u;
            v738 ^= 0x74u;
            v752 ^= 0xB8u;
            v748 ^= 0x50u;
            v756 ^= 0xBDu;
            v754 ^= 0x3Bu;
            v753 ^= 0x39u;
            v734 ^= 0x84u;
            v760 ^= 0xA2u;
            v735 ^= 0x18u;
            v747 ^= 0x7Au;
            v761 ^= 0x8Du;
            v736 ^= 0xAFu;
            v757 ^= 0x86u;
            v763 ^= 0x63u;
            if ( (unsigned int)fksth(&v726, "hAqhVGIrmzYUVUlYGQSYCmFIEkNyEEEckQXMwSt") )
            {
              printf("yllnPTbigC:");
              v3099 = input_val();
              v3100 = input_val();
              v3101 = input_val();
              v3102 = input_val();
              v3103 = input_val();
              v3104 = input_val();
              v3105 = input_val();
            }
            else
            {
              printf("FBErXVnmAH:");
              v3106 = input_val();
              v3107 = input_val();
              v3108 = input_val();
              v3109 = input_val();
              v3110 = input_val();
              v3111 = input_val();
              v3112 = input_val();
            }
            return 0;
          }
        }
      }
      else
      {
        printf("EoWRiWVQYx:");
        v3072 = input_val();
        v3073 = input_val();
        v3074 = input_val();
        v3075 = input_val();
        if ( (v3073 ^ (v3074 * v3075)) == 27144 )
        {
          printf("vAtPOQSGvx:");
          v3068 = input_val();
          v3069 = input_val();
          v3070 = input_val();
          v3071 = input_val();
          if ( v3069 * v3071 == 41942 )
          {
            printf("bjkUdbpJuoCKIXcTS:");
            input_line(&v2066, 0x34uLL);
            v2075 ^= 0xF8u;
            v2086 ^= 0x77u;
            v2092 ^= 0x65u;
            v2109 ^= 0xA9u;
            v2089 ^= 0xDCu;
            v2080 ^= 0xCDu;
            v2097 ^= 0xCEu;
            v2079 ^= 0xA5u;
            v2090 ^= 0xE2u;
            v2107 ^= 0x6Du;
            v2099 ^= 0x49u;
            v2072 ^= 0x3Bu;
            v2112 ^= 0xC1u;
            v2074 ^= 0x80u;
            v2066 ^= 0x43u;
            v2117 ^= 0xC2u;
            v2069 ^= 0xFDu;
            v2094 ^= 0x34u;
            v2076 ^= 0x50u;
            v2091 ^= 0xDDu;
            v2104 ^= 0x32u;
            v2114 ^= 0xCDu;
            v2070 ^= 0x46u;
            v2116 ^= 0x6Fu;
            v2068 ^= 0x11u;
            v2106 ^= 0x64u;
            v2067 ^= 0x83u;
            v2096 ^= 0x20u;
            v2082 ^= 0xCFu;
            v2113 ^= 0x29u;
            v2073 ^= 0x61u;
            v2087 ^= 0xDu;
            v2115 ^= 0xE1u;
            v2102 ^= 0x99u;
            v2078 ^= 0x2Eu;
            v2098 ^= 0x5Du;
            v2108 ^= 0xB6u;
            v2077 ^= 0xFu;
            v2103 ^= 0xE0u;
            v2105 ^= 0x43u;
            v2095 ^= 0xDDu;
            v2101 ^= 0x98u;
            v2085 ^= 0x8Fu;
            v2100 ^= 0xA4u;
            v2088 ^= 0x90u;
            v2084 ^= 0x69u;
            v2081 ^= 0xBDu;
            v2111 ^= 0xA0u;
            v2093 ^= 0x16u;
            v2071 ^= 0x7Eu;
            v2083 ^= 3u;
            v2110 ^= 0xE0u;
            if ( (unsigned int)fksth(&v2066, "GxcYwAoIdliGcuTNCToJZAAcKGraYSHafdoiHdlVjgAxFJSqYXDp") )
            {
              printf("pxJOBuQIKX:");
              v3063 = input_val();
              v3064 = input_val();
              v3065 = input_val();
              v3066 = input_val();
              v3067 = input_val();
            }
            else
            {
              printf("kjXasldKEDhDPJZTRXn:");
              input_line(&v542, 0x24uLL);
              v568 ^= 0x21u;
              v569 ^= 0x6Bu;
              v545 ^= 0x49u;
              v544 ^= 0x66u;
              v565 ^= 0xBu;
              v566 ^= 0x2Bu;
              v551 ^= 0x61u;
              v570 ^= 0x1Au;
              v555 ^= 0x68u;
              v548 ^= 0xABu;
              v547 ^= 0xBDu;
              v560 ^= 0x20u;
              v550 ^= 0xACu;
              v559 ^= 0x11u;
              v567 ^= 0x24u;
              v576 ^= 0x2Fu;
              v577 ^= 0x75u;
              v557 ^= 0x52u;
              v564 ^= 0xCDu;
              v573 ^= 0x8Au;
              v572 ^= 0x99u;
              v542 ^= 0xACu;
              v558 ^= 0xE9u;
              v562 ^= 0x17u;
              v574 ^= 0x1Fu;
              v554 ^= 0x93u;
              v543 ^= 0x76u;
              v556 ^= 0x88u;
              v553 ^= 0xFu;
              v563 ^= 0x83u;
              v552 ^= 0x3Cu;
              v575 ^= 0x38u;
              v561 ^= 0xFu;
              v546 ^= 0xC5u;
              v549 ^= 0x28u;
              v571 ^= 0xBEu;
              fksth(&v542, "BMKRwtAQZIiDkqOLemeFseLHrSVuGftIajCN");
            }
            return 0;
          }
          else
          {
            printf("GSmqFHOFyVvhtYzkvtTJ:");
            input_line(&v2506, 0x3AuLL);
            v2562 ^= 0x82u;
            v2511 ^= 0x72u;
            v2555 ^= 0x8Bu;
            v2527 ^= 8u;
            v2534 ^= 0x61u;
            v2535 ^= 0xB8u;
            v2548 ^= 0xBEu;
            v2551 ^= 0xD6u;
            v2559 ^= 5u;
            v2524 ^= 0xA4u;
            v2526 ^= 0x2Bu;
            v2554 ^= 0x66u;
            v2536 ^= 0x67u;
            v2508 = ~v2508;
            v2537 ^= 0xF5u;
            v2525 ^= 0xC8u;
            v2553 ^= 0xD5u;
            v2560 ^= 0x59u;
            v2533 ^= 0x3Eu;
            v2546 ^= 0xA9u;
            v2552 ^= 0xAu;
            v2516 ^= 0x77u;
            v2561 ^= 4u;
            v2538 ^= 0xA8u;
            v2545 ^= 0xAAu;
            v2550 ^= 0x6Cu;
            v2510 ^= 0x8Fu;
            v2549 ^= 2u;
            v2522 ^= 0xE0u;
            v2506 ^= 0x34u;
            v2547 ^= 0xA6u;
            v2531 ^= 0x32u;
            v2517 ^= 0xEAu;
            v2558 ^= 0xFEu;
            v2515 ^= 0x62u;
            v2541 ^= 0x3Du;
            v2518 ^= 3u;
            v2514 ^= 0x2Du;
            v2507 ^= 0x72u;
            v2523 ^= 0xDu;
            v2540 ^= 0x43u;
            v2528 ^= 0xCAu;
            v2543 ^= 0xA1u;
            v2521 ^= 0x2Bu;
            v2529 ^= 0x28u;
            v2530 ^= 0x8Bu;
            v2513 ^= 0x47u;
            v2563 ^= 0x22u;
            v2509 ^= 0x18u;
            v2520 ^= 0xD3u;
            v2532 ^= 0xB2u;
            v2542 ^= 0xDAu;
            v2519 ^= 0x4Bu;
            v2539 ^= 0x9Fu;
            v2556 ^= 0xCFu;
            v2544 ^= 0xEu;
            v2557 ^= 0xCAu;
            v2512 ^= 0x6Eu;
            if ( (unsigned int)fksth(&v2506, "agBkCibddJQfTgNuFzbMhLXGWJzLeShqaPQgQZHavagogkbTdiEhcGRssE") )
            {
              printf("bJtzBetQVq:");
              v3054 = input_val();
              v3055 = input_val();
              v3056 = input_val();
              v3057 = input_val();
            }
            else
            {
              printf("GMHOOpDQqb:");
              v3058 = input_val();
              v3059 = input_val();
              v3060 = input_val();
              v3061 = input_val();
              v3062 = input_val();
            }
            return 0;
          }
        }
        else
        {
          printf("hVXfMnqoGztFGSEwKuT:");
          input_line(&v299, 0x22uLL);
          v302 ^= 0x8Bu;
          v329 ^= 0x48u;
          v315 ^= 0x57u;
          v316 ^= 0x3Au;
          v326 ^= 0x2Eu;
          v328 ^= 0x4Bu;
          v323 ^= 0x86u;
          v320 ^= 0xA6u;
          v314 ^= 0xDBu;
          v306 ^= 0xDEu;
          v308 ^= 0x5Du;
          v327 ^= 0xEEu;
          v309 ^= 0xD3u;
          v318 ^= 0x32u;
          v313 ^= 0xDAu;
          v325 ^= 0xECu;
          v304 ^= 0xEFu;
          v312 ^= 0x89u;
          v319 ^= 0x8Bu;
          v332 ^= 0xA7u;
          v321 ^= 0xE7u;
          v310 ^= 0x7Bu;
          v317 ^= 0xC7u;
          v322 ^= 0xA4u;
          v303 ^= 0x82u;
          v307 ^= 0xEAu;
          v324 ^= 0xA4u;
          v301 ^= 0xE5u;
          v299 ^= 0xF4u;
          v330 ^= 0xABu;
          v331 ^= 0xE0u;
          v300 ^= 0x1Au;
          v305 ^= 0x76u;
          v311 ^= 0x76u;
          if ( (unsigned int)fksth(&v299, "kjeKNtWOxqzKYkfqjphZiMqtoyMsoqzigu") )
          {
            printf("cvqSUvPzqEhbritpH:");
            input_line(&v333, 0x22uLL);
            v366 ^= 0x62u;
            v361 ^= 0x6Eu;
            v359 ^= 0x2Bu;
            v349 ^= 0x13u;
            v358 ^= 0x14u;
            v356 ^= 0xCu;
            v334 ^= 4u;
            v348 ^= 0xEAu;
            v350 ^= 0xC9u;
            v341 ^= 0x69u;
            v364 ^= 0xBAu;
            v339 ^= 0xF9u;
            v354 ^= 0x12u;
            v360 ^= 0xB6u;
            v336 ^= 0xBEu;
            v338 ^= 0x38u;
            v351 ^= 0x5Eu;
            v355 ^= 0xA4u;
            v365 ^= 0x28u;
            v333 ^= 0x27u;
            v353 ^= 0xA0u;
            v357 ^= 0xF7u;
            v347 ^= 0x42u;
            v344 ^= 0xA7u;
            v362 ^= 0x1Du;
            v352 ^= 0x23u;
            v346 ^= 0xC9u;
            v340 ^= 0x93u;
            v337 ^= 0xD0u;
            v345 ^= 0x64u;
            v363 ^= 0x6Cu;
            v343 ^= 0x7Cu;
            v342 ^= 0xBDu;
            v335 ^= 0xBBu;
            if ( (unsigned int)fksth(&v333, "FNvObuHSFvEAMThbpmzHcbTmUixwFexLwr") )
            {
              printf("QtwikkDPSzE:");
              input_line(&v1817, 0x31uLL);
              v1825 ^= 0x54u;
              v1817 ^= 0x75u;
              v1839 ^= 0xCFu;
              v1842 ^= 0x54u;
              v1832 ^= 0x47u;
              v1855 ^= 0x43u;
              v1830 ^= 0x66u;
              v1854 ^= 0x15u;
              v1850 ^= 0x5Fu;
              v1820 ^= 0x50u;
              v1833 = ~v1833;
              v1848 ^= 0xAAu;
              v1827 ^= 0x32u;
              v1838 ^= 0x98u;
              v1841 ^= 0x1Fu;
              v1849 ^= 0xDAu;
              v1821 ^= 0xBu;
              v1857 ^= 0x32u;
              v1826 ^= 0xC2u;
              v1863 ^= 0xF8u;
              v1843 ^= 0xE0u;
              v1822 ^= 0x90u;
              v1823 ^= 0x6Au;
              v1831 ^= 0x1Au;
              v1818 ^= 0xC8u;
              v1847 ^= 0x85u;
              v1844 ^= 0x3Fu;
              v1865 ^= 0x1Au;
              v1836 ^= 0xDu;
              v1846 ^= 0xBCu;
              v1819 ^= 0xC7u;
              v1852 ^= 0x7Fu;
              v1845 ^= 0x31u;
              v1851 ^= 0x97u;
              v1860 ^= 4u;
              v1858 ^= 0x6Au;
              v1837 ^= 0x3Fu;
              v1856 ^= 0x91u;
              v1853 ^= 0x52u;
              v1861 ^= 0x97u;
              v1835 ^= 0xDAu;
              v1840 ^= 0xACu;
              v1859 ^= 0xB8u;
              v1824 ^= 0xBCu;
              v1864 ^= 0x90u;
              v1829 ^= 0xAu;
              v1828 ^= 0xE5u;
              v1834 ^= 0x40u;
              v1862 ^= 0xD0u;
              fksth(&v1817, "JrFYtqaobJbkMWXmhxkmnfpLvCpYeDvvLpFWRTRhkXmJJhLJc");
            }
            else
            {
              printf("fFDZYIuBZA:");
              v3043 = input_val();
              v3044 = input_val();
              v3045 = input_val();
              v3046 = input_val();
            }
            return 0;
          }
          else
          {
            printf("FYtJMzBIdIqsGHDqGGO:");
            input_line(&v877, 0x29uLL);
            v902 ^= 0xA3u;
            v912 ^= 0x2Eu;
            v885 ^= 0xFCu;
            v887 ^= 0x93u;
            v907 ^= 0x5Cu;
            v899 ^= 0x39u;
            v884 ^= 0x78u;
            v880 ^= 0x2Au;
            v879 ^= 0x55u;
            v901 ^= 0xB8u;
            v889 ^= 0x7Bu;
            v888 ^= 0x1Bu;
            v896 ^= 0xB9u;
            v909 ^= 0x9Fu;
            v883 ^= 0xAAu;
            v913 ^= 8u;
            v914 ^= 0x25u;
            v892 ^= 0x9Fu;
            v915 ^= 0x17u;
            v894 ^= 0x4Du;
            v908 ^= 0xF1u;
            v906 ^= 0x51u;
            v897 ^= 0xAu;
            v898 ^= 0xB7u;
            v890 ^= 0x83u;
            v903 ^= 0xA5u;
            v895 ^= 0xD4u;
            v916 ^= 0x6Cu;
            v904 ^= 0xE2u;
            v905 ^= 0x3Cu;
            v877 ^= 0x86u;
            v882 ^= 0x1Cu;
            v893 ^= 0x74u;
            v891 ^= 0xC0u;
            v878 ^= 0xEAu;
            v886 ^= 0x84u;
            v917 ^= 0x20u;
            v900 ^= 0x8Eu;
            v910 ^= 0x65u;
            v881 ^= 0x75u;
            v911 ^= 0x99u;
            if ( (unsigned int)fksth(&v877, "nLETbWqMvAFxNLNylVwinBWlaSXmeBRsTSNDDDLnd") )
            {
              printf("ssqRUscnDO:");
              v3047 = input_val();
              v3048 = input_val();
              v3049 = input_val();
              v3050 = input_val();
              v3051 = input_val();
              v3052 = input_val();
              v3053 = input_val();
            }
            else
            {
              printf("QgFqgOBmteCwFtoSNvrs:");
              input_line(&v1768, 0x31uLL);
              v1793 ^= 0xD3u;
              v1815 ^= 7u;
              v1791 ^= 0x2Fu;
              v1803 ^= 0x5Cu;
              v1798 ^= 0x46u;
              v1775 ^= 0xE7u;
              v1802 ^= 0xEu;
              v1814 ^= 0xBu;
              v1773 ^= 0xA7u;
              v1780 ^= 0x23u;
              v1776 ^= 0xB5u;
              v1805 ^= 0x8Fu;
              v1769 ^= 0xE0u;
              v1799 ^= 0x46u;
              v1789 ^= 0xCEu;
              v1811 ^= 0x24u;
              v1800 ^= 0x97u;
              v1794 ^= 0xE4u;
              v1778 ^= 0x71u;
              v1797 ^= 0xB8u;
              v1785 ^= 0xB9u;
              v1792 ^= 0xB3u;
              v1777 ^= 0xF8u;
              v1812 ^= 0xC3u;
              v1816 ^= 0xA0u;
              v1784 ^= 0xA8u;
              v1795 ^= 0x85u;
              v1807 ^= 0xBBu;
              v1801 ^= 0xDCu;
              v1787 ^= 0x88u;
              v1804 ^= 0xFAu;
              v1770 ^= 0x79u;
              v1810 ^= 0xAu;
              v1809 ^= 0xCCu;
              v1796 ^= 0x1Cu;
              v1768 ^= 0x38u;
              v1788 ^= 0x8Au;
              v1790 ^= 0xA0u;
              v1781 ^= 0x1Eu;
              v1779 ^= 0x76u;
              v1772 ^= 0xC7u;
              v1813 ^= 0x69u;
              v1806 ^= 0x82u;
              v1808 ^= 0xDu;
              v1774 ^= 0xF8u;
              v1782 ^= 0xBFu;
              v1771 ^= 0x64u;
              v1783 ^= 0x82u;
              v1786 ^= 0xF0u;
              fksth(&v1768, "LJWeGZBUzMzTywkufmBsXOhUzwuSTOeWxrprEXrmRSDODUtuJ");
            }
            return 0;
          }
        }
      }
    }
  }
  else
  {
    printf("qqxWcLuvhA:");
    v3375 = input_val();
    v3376 = input_val();
    v3377 = input_val();
    v3378 = input_val();
    v3379 = input_val();
    v3380 = input_val();
    if ( v3376 + v3377 * v3378 == 34943 )
    {
      printf("vafdxbGPIP:");
      v3368 = input_val();
      v3369 = input_val();
      v3370 = input_val();
      v3371 = input_val();
      v3372 = input_val();
      v3373 = input_val();
      v3374 = input_val();
      if ( ((v3371 - v3374) ^ v3369) == 40290 )
      {
        printf("xRvNybxSOwCgIkzvj:");
        input_line(&v1439, 0x2EuLL);
        v1484 ^= 0x5Eu;
        v1466 ^= 0x65u;
        v1452 ^= 0xB7u;
        v1441 ^= 0x73u;
        v1481 ^= 0xDAu;
        v1472 ^= 0xE3u;
        v1467 ^= 0x95u;
        v1443 ^= 0x60u;
        v1474 ^= 0x57u;
        v1461 ^= 0x26u;
        v1464 ^= 0x8Eu;
        v1445 ^= 0x48u;
        v1465 ^= 0xF5u;
        v1451 ^= 0x60u;
        v1442 ^= 0x16u;
        v1462 ^= 0xCBu;
        v1477 ^= 0xC9u;
        v1475 ^= 0x37u;
        v1456 ^= 0x88u;
        v1450 ^= 0x60u;
        v1478 ^= 0x67u;
        v1449 ^= 0x29u;
        v1458 ^= 0xDDu;
        v1453 ^= 0xE0u;
        v1444 ^= 0x36u;
        v1460 ^= 0x19u;
        v1483 = ~v1483;
        v1459 ^= 0xD2u;
        v1479 ^= 0x98u;
        v1476 ^= 0x4Eu;
        v1448 ^= 0xA6u;
        v1480 ^= 0xD8u;
        v1439 ^= 0xF4u;
        v1473 ^= 0xB0u;
        v1455 ^= 0x6Eu;
        v1482 ^= 0x49u;
        v1463 ^= 0xEAu;
        v1471 ^= 0x96u;
        v1468 ^= 0xCAu;
        v1447 ^= 0x5Bu;
        v1454 ^= 0x8Bu;
        v1440 ^= 0xF9u;
        v1470 ^= 0x75u;
        v1446 ^= 0xB6u;
        v1469 ^= 0xD5u;
        v1457 ^= 0x72u;
        if ( (unsigned int)fksth(&v1439, "bUCcQlMeVZtvLYMJagdQowGEqVPyoUSZLIlStRfScyccuB") )
        {
          printf("zUHHLdLnBqlkECD:");
          input_line(&v1577, 0x2FuLL);
          v1588 ^= 0xC2u;
          v1606 ^= 0xFu;
          v1607 ^= 0xE6u;
          v1616 ^= 0xDEu;
          v1582 ^= 0x8Cu;
          v1589 ^= 0x94u;
          v1600 ^= 0xAEu;
          v1583 ^= 0x77u;
          v1579 ^= 0x1Au;
          v1611 ^= 0x79u;
          v1609 ^= 0xEDu;
          v1587 ^= 6u;
          v1621 ^= 0xC1u;
          v1613 ^= 0xA9u;
          v1584 ^= 0xAEu;
          v1620 ^= 0xAAu;
          v1580 ^= 0x8Fu;
          v1602 ^= 0x85u;
          v1595 ^= 9u;
          v1604 ^= 0x64u;
          v1615 ^= 0x8Fu;
          v1585 ^= 0x2Du;
          v1592 ^= 0x94u;
          v1605 ^= 0x40u;
          v1623 ^= 0x73u;
          v1601 ^= 0xC0u;
          v1610 ^= 0x20u;
          v1593 ^= 0xBEu;
          v1608 ^= 7u;
          v1612 ^= 0x58u;
          v1598 ^= 0xE7u;
          v1577 ^= 0x55u;
          v1581 ^= 0xA8u;
          v1596 ^= 0x62u;
          v1590 ^= 0xC1u;
          v1594 ^= 3u;
          v1578 ^= 0x9Au;
          v1618 ^= 0xAEu;
          v1591 ^= 0x72u;
          v1622 ^= 0x26u;
          v1614 ^= 0xB5u;
          v1599 ^= 0xAAu;
          v1617 ^= 0x22u;
          v1603 ^= 0xCEu;
          v1619 ^= 0x1Bu;
          v1586 ^= 0xF2u;
          v1597 ^= 0xD5u;
          if ( (unsigned int)fksth(&v1577, "kyyFxBAJfUWYrrebzVbwSHjLuoYbmNMZLuVXWyVrtRdOWEb") )
          {
            printf("hPFHNgRBYY:");
            input_line(&v2741, 0x3CuLL);
            v2774 ^= 0x40u;
            v2756 ^= 0xEDu;
            v2761 ^= 0xBBu;
            v2771 ^= 0x64u;
            v2773 ^= 0xACu;
            v2785 ^= 0x32u;
            v2787 ^= 0x7Fu;
            v2790 ^= 0x74u;
            v2752 ^= 0xB2u;
            v2767 ^= 0xBDu;
            v2750 ^= 0x91u;
            v2783 ^= 0x20u;
            v2795 ^= 0x73u;
            v2781 ^= 0xBu;
            v2753 ^= 0x2Fu;
            v2760 ^= 0xC9u;
            v2758 ^= 0x91u;
            v2775 ^= 0xA1u;
            v2748 ^= 0xE7u;
            v2755 ^= 0x64u;
            v2751 ^= 0x80u;
            v2770 ^= 0x36u;
            v2779 ^= 0x98u;
            v2797 ^= 0xAFu;
            v2796 ^= 0xA4u;
            v2747 ^= 0xA1u;
            v2769 ^= 0x28u;
            v2777 ^= 0x4Cu;
            v2744 ^= 0x52u;
            v2766 ^= 0xE6u;
            v2778 ^= 0xAAu;
            v2784 ^= 0x9Au;
            v2764 ^= 0x37u;
            v2786 ^= 0x22u;
            v2782 ^= 0x14u;
            v2746 ^= 0x23u;
            v2789 ^= 0xDCu;
            v2745 ^= 0x8Bu;
            v2749 ^= 0x4Du;
            v2762 ^= 0x86u;
            v2776 ^= 0x91u;
            v2792 ^= 0x64u;
            v2793 ^= 0xDBu;
            v2765 ^= 0x96u;
            v2757 ^= 0x40u;
            v2742 ^= 0x24u;
            v2788 ^= 0x53u;
            v2768 ^= 0xF0u;
            v2798 ^= 0xF6u;
            v2780 ^= 0x36u;
            v2763 ^= 0xA0u;
            v2743 ^= 0xF8u;
            v2799 ^= 0xF1u;
            v2794 ^= 0x2Du;
            v2791 ^= 0xA5u;
            v2759 ^= 0xC0u;
            v2772 ^= 0xD9u;
            v2754 ^= 0xC1u;
            v2741 ^= 0x9Bu;
            if ( (unsigned int)fksth(&v2741, "OnAVwtiUQdBQLgWSfqbmrWboyhEAVCsnxnBmXevHLlwvSsbcZiZSemiyJYkU") )
            {
              printf("xmhZgBvGxnXfukLhtheP:");
              input_line(&v1671, 0x30uLL);
              v1706 ^= 0xCu;
              v1718 ^= 0xBDu;
              v1681 ^= 0x79u;
              v1691 ^= 0xDu;
              v1688 ^= 0x38u;
              v1671 ^= 0xF5u;
              v1702 ^= 0x64u;
              v1697 ^= 0x74u;
              v1703 ^= 0xA3u;
              v1708 ^= 0xADu;
              v1677 ^= 0x90u;
              v1685 ^= 0x71u;
              v1673 ^= 1u;
              v1693 ^= 0x23u;
              v1678 ^= 0x1Du;
              v1716 ^= 0x77u;
              v1683 ^= 0x35u;
              v1704 ^= 0x9Cu;
              v1701 ^= 0xE4u;
              v1682 ^= 0x4Du;
              v1687 ^= 0x76u;
              v1699 ^= 0xA3u;
              v1679 ^= 0xF8u;
              v1717 = ~v1717;
              v1689 ^= 0xCBu;
              v1694 ^= 0x10u;
              v1710 ^= 0xCFu;
              v1711 ^= 0xF5u;
              v1714 ^= 0x4Cu;
              v1705 ^= 0xE5u;
              v1680 ^= 0xEAu;
              v1696 ^= 0xA9u;
              v1712 ^= 0x47u;
              v1674 ^= 0x59u;
              v1686 ^= 0x74u;
              v1676 ^= 6u;
              v1715 ^= 0x90u;
              v1709 ^= 0xA5u;
              v1698 ^= 0x64u;
              v1707 ^= 0xB5u;
              v1700 ^= 0xFDu;
              v1684 ^= 0x49u;
              v1690 ^= 0x78u;
              v1695 ^= 0xC5u;
              v1672 ^= 0x72u;
              v1675 ^= 0xBCu;
              v1713 ^= 0xD3u;
              v1692 ^= 0xC1u;
              fksth(&v1671, "ruSfqQtmhSRVdFvhbUfhMIQHRGRJyGRPLIbWfUTNCfcBbGvk");
            }
            else
            {
              printf("jbGOZDeljB:");
              v44 = input_val();
              v45 = input_val();
              v46 = input_val();
              v47 = input_val();
              v48 = input_val();
              v49 = input_val();
              v50 = input_val();
              v51 = input_val();
            }
            return 0;
          }
          else
          {
            printf("HcCJZzdjJzr:");
            input_line(&v2623, 0x3BuLL);
            v2674 ^= 0xEFu;
            v2630 ^= 0x49u;
            v2667 ^= 0xA4u;
            v2628 ^= 0xB7u;
            v2672 ^= 0x4Eu;
            v2634 ^= 0x7Cu;
            v2669 ^= 0xC5u;
            v2637 ^= 0x6Du;
            v2638 ^= 0x4Du;
            v2678 ^= 0xBDu;
            v2626 ^= 0x3Cu;
            v2645 ^= 0xEDu;
            v2656 ^= 0xA1u;
            v2653 ^= 0xF8u;
            v2648 ^= 0x21u;
            v2640 ^= 0x74u;
            v2629 ^= 0xD2u;
            v2662 ^= 0x30u;
            v2673 ^= 0x5Bu;
            v2660 ^= 0xAu;
            v2670 ^= 0x60u;
            v2627 ^= 0xC5u;
            v2657 ^= 0x3Bu;
            v2655 ^= 0xB7u;
            v2663 ^= 0xFCu;
            v2642 ^= 0x41u;
            v2644 ^= 0x60u;
            v2624 ^= 0xA5u;
            v2651 ^= 0x3Bu;
            v2635 ^= 0xC8u;
            v2661 ^= 0x7Fu;
            v2665 ^= 0xE4u;
            v2633 ^= 0xCEu;
            v2652 ^= 0x28u;
            v2650 ^= 0x57u;
            v2646 ^= 0xE4u;
            v2658 ^= 0x3Fu;
            v2639 ^= 0xFDu;
            v2668 ^= 0x43u;
            v2625 ^= 0x80u;
            v2643 ^= 0xCEu;
            v2677 ^= 0x8Du;
            v2679 ^= 0xB2u;
            v2681 ^= 0x6Au;
            v2671 ^= 0x1Au;
            v2641 ^= 0x3Eu;
            v2680 ^= 0xCFu;
            v2654 ^= 0x8Fu;
            v2649 ^= 0x16u;
            v2675 ^= 0x8Bu;
            v2666 ^= 0xC5u;
            v2623 ^= 0x2Au;
            v2632 ^= 0x63u;
            v2664 ^= 0x8Bu;
            v2636 ^= 0x8Fu;
            v2647 ^= 0x63u;
            v2631 ^= 0x8Du;
            v2676 ^= 0xCu;
            v2659 ^= 9u;
            if ( (unsigned int)fksth(&v2623, "TnHxZgkTtqPRhfIXBoECuGTaAbSOoNFVHvoZSumdvhxZcTjPKYGiWIeBttl") )
            {
              printf("QlSBsEEzRI:");
              v36 = input_val();
              v37 = input_val();
              v38 = input_val();
              v39 = input_val();
              v40 = input_val();
              v41 = input_val();
              v42 = input_val();
              v43 = input_val();
            }
            else
            {
              printf("HYdNyuiMXecqHZhHDBNe:");
              input_line(&v1174, 0x2CuLL);
              v1181 ^= 0xC4u;
              v1199 ^= 0x8Eu;
              v1201 ^= 0xBDu;
              v1198 ^= 0x1Cu;
              v1191 ^= 0x68u;
              v1212 ^= 0x55u;
              v1183 ^= 0xCEu;
              v1202 ^= 0x59u;
              v1175 ^= 0xD3u;
              v1186 ^= 0xFEu;
              v1207 ^= 3u;
              v1216 ^= 0x44u;
              v1190 ^= 0x6Fu;
              v1200 ^= 0x45u;
              v1217 ^= 0x43u;
              v1189 ^= 0xE5u;
              v1208 ^= 0x95u;
              v1197 ^= 0x5Fu;
              v1180 ^= 0x37u;
              v1179 ^= 0x20u;
              v1210 ^= 0xDCu;
              v1192 ^= 0xDBu;
              v1214 ^= 0x21u;
              v1203 ^= 0xBCu;
              v1213 ^= 0x45u;
              v1209 ^= 0xA4u;
              v1188 ^= 0xA3u;
              v1185 ^= 0xEDu;
              v1211 ^= 0xB6u;
              v1193 ^= 0xBBu;
              v1204 ^= 0x75u;
              v1206 ^= 0xD0u;
              v1205 ^= 0xF4u;
              v1195 ^= 0xB1u;
              v1182 ^= 0x58u;
              v1187 ^= 0xC1u;
              v1196 ^= 0xEDu;
              v1174 ^= 0xD9u;
              v1184 ^= 0xD2u;
              v1194 ^= 0xEBu;
              v1215 ^= 0x8Cu;
              v1177 ^= 0xF5u;
              v1178 ^= 0x2Bu;
              v1176 ^= 0x9Du;
              fksth(&v1174, "GTtnIeMCtXKQnvEACQGHwsOkivjGkYGcRercFiJfGGnw");
            }
            return 0;
          }
        }
        else
        {
          printf("KWItlUXOdO:");
          input_line(&v4, 0x20uLL);
          v11 ^= 0xD1u;
          v7 ^= 0xA9u;
          v29 ^= 0x74u;
          v20 ^= 0xA7u;
          v26 ^= 0xD1u;
          v31 ^= 0xC3u;
          v22 ^= 0xD1u;
          v25 ^= 0x5Du;
          v9 ^= 0x92u;
          v17 ^= 0xAEu;
          v18 ^= 0xFDu;
          v8 ^= 0x70u;
          v5 ^= 0x7Cu;
          v14 ^= 0x6Fu;
          v19 ^= 0x2Bu;
          v23 ^= 0x86u;
          v10 ^= 0x2Eu;
          v34 ^= 0xD9u;
          v21 ^= 0xB1u;
          v16 ^= 5u;
          v27 ^= 0x57u;
          v4 ^= 0xDCu;
          v6 ^= 0x82u;
          v35 ^= 0x40u;
          v12 ^= 0x76u;
          v24 ^= 0xA9u;
          v15 ^= 0x6Cu;
          v28 ^= 0x84u;
          v30 ^= 0xBBu;
          v33 ^= 1u;
          v32 ^= 0x57u;
          v13 ^= 0xE1u;
          if ( (unsigned int)fksth(&v4, "ICyOgliaHiVMBegGjZPKHHcejBhIbydM") )
          {
            printf("QqsPmcRCJZqAbsPaMCgM:");
            input_line(&v1045, 0x2BuLL);
            v1057 ^= 0xB4u;
            v1085 ^= 3u;
            v1048 ^= 0x8Bu;
            v1061 ^= 0x87u;
            v1076 ^= 0x22u;
            v1069 ^= 0x42u;
            v1059 ^= 0x9Au;
            v1063 ^= 0xC4u;
            v1075 ^= 7u;
            v1079 ^= 0xEDu;
            v1071 ^= 0xCAu;
            v1080 ^= 0x1Bu;
            v1058 ^= 0x3Au;
            v1082 ^= 0xCCu;
            v1050 ^= 0x34u;
            v1047 ^= 0x70u;
            v1045 ^= 0x2Eu;
            v1049 = ~v1049;
            v1066 ^= 0x77u;
            v1073 ^= 0x92u;
            v1067 ^= 0xFAu;
            v1074 ^= 0x33u;
            v1065 ^= 0x9Du;
            v1051 ^= 0x61u;
            v1087 ^= 5u;
            v1060 ^= 0x1Au;
            v1070 ^= 0xADu;
            v1056 ^= 0xCCu;
            v1083 ^= 0x34u;
            v1077 ^= 0xE3u;
            v1055 ^= 0x3Bu;
            v1084 ^= 0xBFu;
            v1054 ^= 0xC0u;
            v1086 ^= 0x2Cu;
            v1081 ^= 0x43u;
            v1064 ^= 0xAEu;
            v1053 ^= 0xCCu;
            v1072 ^= 0x9Eu;
            v1078 ^= 0xE8u;
            v1062 ^= 0xCFu;
            v1052 ^= 0xC6u;
            v1068 ^= 0xE1u;
            v1046 ^= 0x40u;
            if ( (unsigned int)fksth(&v1045, "XPwDZFSNYzTfbsDxTQcOwBKgynwLSVCxtwUkQBjqirn") )
            {
              printf("hpbRlolqPF:");
              v3357 = input_val();
              v3358 = input_val();
              v3359 = input_val();
              v3360 = input_val();
              v3361 = input_val();
            }
            else
            {
              printf("nPTvfAUJcsTebdd:");
              input_line(&v2564, 0x3BuLL);
              v2565 ^= 0xA3u;
              v2567 ^= 0x38u;
              v2573 = ~v2573;
              v2619 ^= 0x4Bu;
              v2592 ^= 0xDBu;
              v2574 ^= 0x39u;
              v2622 ^= 0xC8u;
              v2606 ^= 0x94u;
              v2588 ^= 0x3Fu;
              v2587 ^= 0x74u;
              v2613 ^= 0xEFu;
              v2570 ^= 0xD2u;
              v2603 ^= 0xE8u;
              v2610 ^= 0xFDu;
              v2616 ^= 0x45u;
              v2590 ^= 0xC2u;
              v2621 ^= 0x33u;
              v2572 ^= 0xB4u;
              v2602 ^= 0xD5u;
              v2578 ^= 0xD1u;
              v2620 ^= 0x66u;
              v2597 ^= 0x84u;
              v2601 ^= 0xE5u;
              v2596 ^= 0xCFu;
              v2576 ^= 0x48u;
              v2615 ^= 0x13u;
              v2582 ^= 0xD5u;
              v2566 ^= 0xC7u;
              v2614 ^= 0x60u;
              v2581 ^= 0x19u;
              v2608 ^= 0x7Cu;
              v2577 ^= 0x97u;
              v2595 ^= 0x65u;
              v2589 ^= 0x60u;
              v2604 ^= 0xCFu;
              v2607 ^= 0x77u;
              v2569 ^= 0xFDu;
              v2583 ^= 0xE7u;
              v2580 ^= 0x26u;
              v2571 ^= 0x3Bu;
              v2599 ^= 0x26u;
              v2568 ^= 0xC7u;
              v2575 ^= 0xAEu;
              v2586 ^= 0x6Eu;
              v2593 ^= 0xC8u;
              v2579 ^= 2u;
              v2584 ^= 0x68u;
              v2564 ^= 0x71u;
              v2585 ^= 9u;
              v2611 ^= 0xF1u;
              v2605 ^= 0x96u;
              v2612 ^= 0xEEu;
              v2598 ^= 0x66u;
              v2600 ^= 0xC0u;
              v2609 ^= 0x76u;
              v2594 ^= 0x46u;
              v2618 ^= 0xF4u;
              v2617 ^= 0x27u;
              v2591 ^= 0xACu;
              fksth(&v2564, "MQSMMyYODbHlQbtDZCJGsVlzHfVfINuFApMSIiGIxDbBaZsLMyjZIhfujJZ");
            }
            return 0;
          }
          else
          {
            printf("GOJIaxcCSM:");
            v3362 = input_val();
            v3363 = input_val();
            v3364 = input_val();
            v3365 = input_val();
            v3366 = input_val();
            v3367 = input_val();
            if ( v3364 * v3362 + v3365 == 8990 )
            {
              printf("NUjOmdgUMmDIlT:");
              input_line(&v1131, 0x2CuLL);
              v1145 ^= 0xE2u;
              v1136 ^= 0x89u;
              v1170 ^= 0xC0u;
              v1156 ^= 0xA5u;
              v1158 ^= 0x85u;
              v1172 ^= 0xAEu;
              v1147 ^= 0x8Au;
              v1163 ^= 0x8Cu;
              v1173 ^= 0x41u;
              v1139 ^= 0x6Bu;
              v1162 ^= 0xB6u;
              v1168 ^= 0xCAu;
              v1137 ^= 0xEFu;
              v1140 ^= 0x1Eu;
              v1169 ^= 0xECu;
              v1154 ^= 0x62u;
              v1171 ^= 0x14u;
              v1133 ^= 0xAAu;
              v1167 ^= 0xECu;
              v1146 ^= 0xA3u;
              v1134 ^= 0x23u;
              v1159 ^= 0xFBu;
              v1144 ^= 0x3Fu;
              v1143 ^= 0xD8u;
              v1155 ^= 0xB0u;
              v1166 ^= 0x5Fu;
              v1135 ^= 0xB3u;
              v1153 ^= 0x32u;
              v1160 ^= 0x14u;
              v1132 ^= 0xE9u;
              v1165 ^= 0xD0u;
              v1149 ^= 0x66u;
              v1164 ^= 0xB6u;
              v1152 ^= 0x6Au;
              v1148 ^= 0x28u;
              v1131 ^= 0x6Fu;
              v1151 ^= 8u;
              v1161 ^= 0x2Au;
              v1150 ^= 0xDFu;
              v1142 ^= 0x1Fu;
              v1138 ^= 0x1Bu;
              v1157 ^= 0x94u;
              v1141 ^= 0x8Cu;
              fksth(&v1131, "JcwgKtLOWHWsGSOajqsfNmVUvuiIeFOzGankfHfjGVGc");
            }
            else
            {
              printf("LvyoXWwsDOxWamepWE:");
              input_line(&v1002, 0x2BuLL);
              v1032 ^= 0xC4u;
              v1020 ^= 0x9Eu;
              v1028 ^= 0x9Du;
              v1003 ^= 0x32u;
              v1009 ^= 0x6Au;
              v1021 ^= 0x54u;
              v1014 ^= 0x20u;
              v1011 ^= 0xA9u;
              v1023 ^= 0xA1u;
              v1030 ^= 0x3Eu;
              v1044 ^= 0x56u;
              v1041 ^= 0xF5u;
              v1007 ^= 0xAEu;
              v1010 ^= 0xE7u;
              v1015 ^= 0x30u;
              v1004 ^= 0x8Fu;
              v1039 ^= 0x60u;
              v1002 ^= 0xEDu;
              v1036 ^= 0x1Au;
              v1026 ^= 0xAEu;
              v1034 ^= 0x69u;
              v1025 ^= 0x71u;
              v1040 ^= 0xADu;
              v1012 ^= 0x2Du;
              v1035 ^= 0x60u;
              v1033 ^= 0xD4u;
              v1006 ^= 0x8Au;
              v1005 ^= 0x24u;
              v1029 ^= 0xD3u;
              v1024 ^= 0xB9u;
              v1042 ^= 0xB9u;
              v1018 ^= 0x61u;
              v1043 ^= 0xF9u;
              v1016 ^= 0x92u;
              v1038 ^= 0x56u;
              v1037 ^= 0xB0u;
              v1013 ^= 0x4Eu;
              v1008 ^= 0x3Eu;
              v1027 ^= 0x2Au;
              v1019 ^= 0x7Du;
              v1017 ^= 0x79u;
              v1031 ^= 0x79u;
              v1022 ^= 0x15u;
              fksth(&v1002, "iIeDMKDWhrAKDBwadBftyTwOXpHgYLNvsNikkBShsEo");
            }
            return 0;
          }
        }
      }
      else
      {
        printf("nciNHrvzZGodTixLgIqq:");
        input_line(&v3326, 0x1FuLL);
        v3329 ^= 0x17u;
        v3351 ^= 0x28u;
        v3327 ^= 0xE8u;
        v3336 ^= 0x49u;
        v3349 ^= 0xCEu;
        v3347 ^= 0xC4u;
        v3340 ^= 0x2Du;
        v3344 ^= 0x3Fu;
        v3333 ^= 0x2Au;
        v3356 ^= 0xD6u;
        v3350 ^= 0xF4u;
        v3337 ^= 0xCFu;
        v3330 ^= 0xA6u;
        v3352 ^= 0x94u;
        v3331 ^= 0xA4u;
        v3341 ^= 0xFCu;
        v3335 ^= 0xA3u;
        v3355 ^= 0x5Du;
        v3326 ^= 0x93u;
        v3342 ^= 0xE8u;
        v3353 ^= 0x38u;
        v3354 ^= 0xF0u;
        v3339 ^= 0x3Cu;
        v3346 ^= 0xBFu;
        v3338 ^= 0x8Eu;
        v3334 ^= 0x2Du;
        v3348 ^= 0xDCu;
        v3328 ^= 0xF4u;
        v3343 ^= 0x78u;
        v3332 ^= 0x51u;
        v3345 ^= 0xF3u;
        if ( (unsigned int)fksth(&v3326, "NOzdsHpaRAlQryWoQWRTahIzGGidKQf") )
        {
          printf("FyAbTrmmixGdLG:");
          input_line(&v401, 0x23uLL);
          v423 ^= 0x1Cu;
          v406 ^= 0xB9u;
          v403 ^= 0x46u;
          v425 ^= 0xEDu;
          v424 ^= 0xC5u;
          v433 ^= 0xCAu;
          v417 ^= 0x7Au;
          v431 ^= 4u;
          v420 ^= 0x6Eu;
          v405 ^= 0x29u;
          v411 ^= 0x4Fu;
          v428 ^= 0x46u;
          v421 ^= 0x45u;
          v422 ^= 0x58u;
          v429 ^= 0x7Cu;
          v407 ^= 0xBEu;
          v416 ^= 0xF8u;
          v427 ^= 0xF5u;
          v418 ^= 0xEBu;
          v402 ^= 0x1Au;
          v426 ^= 0xEBu;
          v430 ^= 0xD6u;
          v413 ^= 0xF1u;
          v408 ^= 0x6Eu;
          v412 ^= 0xFBu;
          v410 ^= 0xBDu;
          v419 ^= 0xFEu;
          v434 ^= 0xBu;
          v409 ^= 0x60u;
          v404 ^= 0xA7u;
          v414 ^= 0xE5u;
          v432 ^= 0xEu;
          v401 ^= 0x39u;
          v415 ^= 0x32u;
          if ( (unsigned int)fksth(&v401, "aldClapyBBQYtmpYbgoIZJwTESFyGXcAjHA") )
          {
            printf("MeowQUoosw:");
            input_line(&v165, 0x21uLL);
            v183 ^= 0xB5u;
            v187 ^= 0xDFu;
            v173 ^= 0x5Au;
            v168 ^= 0xE6u;
            v181 ^= 0x4Fu;
            v171 ^= 0xE3u;
            v169 ^= 0x6Du;
            v180 ^= 0xD0u;
            v197 ^= 0x84u;
            v172 ^= 0x31u;
            v166 ^= 0x16u;
            v194 ^= 0x42u;
            v189 ^= 0x55u;
            v178 ^= 0x6Du;
            v176 ^= 0xF7u;
            v185 ^= 0xC8u;
            v188 ^= 0x69u;
            v193 ^= 0x36u;
            v167 ^= 0x28u;
            v196 ^= 0x5Du;
            v174 ^= 0x30u;
            v186 ^= 0x2Cu;
            v170 ^= 0xD3u;
            v190 ^= 0xBBu;
            v191 ^= 0x57u;
            v175 ^= 0x32u;
            v179 ^= 0x18u;
            v184 ^= 0x47u;
            v192 ^= 0xCAu;
            v165 ^= 0xCEu;
            v177 ^= 0xFBu;
            v195 ^= 0xD6u;
            v182 ^= 0x12u;
            if ( (unsigned int)fksth(&v165, "ugIWmzIXQOlHLJcxUezWCMOTXvdrzfbgv") )
            {
              printf("uIXbZHEzsaeXe:");
              input_line(&v2170, 0x36uLL);
              v2211 ^= 0x3Eu;
              v2208 ^= 0xC9u;
              v2196 ^= 0xF4u;
              v2218 ^= 0xAu;
              v2173 ^= 0x69u;
              v2189 ^= 0x1Fu;
              v2201 ^= 0x13u;
              v2206 ^= 0x21u;
              v2177 ^= 0xD0u;
              v2195 ^= 0xD7u;
              v2214 ^= 0x8Cu;
              v2179 ^= 0xCAu;
              v2210 ^= 0x9Cu;
              v2180 ^= 0x4Bu;
              v2191 ^= 0xABu;
              v2182 ^= 0x5Du;
              v2199 ^= 0xAu;
              v2223 ^= 0xDFu;
              v2198 ^= 0xC4u;
              v2181 ^= 0x22u;
              v2186 ^= 0x2Du;
              v2221 ^= 0x1Au;
              v2207 ^= 0xD4u;
              v2183 ^= 0x75u;
              v2178 ^= 0x6Bu;
              v2200 ^= 0x2Eu;
              v2187 ^= 0x4Cu;
              v2193 ^= 0x56u;
              v2194 ^= 0xAEu;
              v2220 ^= 0x59u;
              v2174 ^= 0x15u;
              v2216 ^= 0xC7u;
              v2184 ^= 0x46u;
              v2170 ^= 0xFAu;
              v2176 ^= 0x79u;
              v2175 ^= 0x8Au;
              v2217 ^= 0xDEu;
              v2172 ^= 0xDBu;
              v2188 ^= 0x91u;
              v2209 ^= 0xC3u;
              v2215 ^= 0xFEu;
              v2190 ^= 7u;
              v2204 ^= 0x6Cu;
              v2205 ^= 0x11u;
              v2192 ^= 0x4Bu;
              v2185 ^= 0xB6u;
              v2202 ^= 0xFEu;
              v2197 ^= 0x81u;
              v2213 ^= 0xA1u;
              v2222 ^= 0xF0u;
              v2171 ^= 0x14u;
              v2203 ^= 0x8Au;
              v2212 ^= 0xF1u;
              v2219 ^= 0xEAu;
              fksth(&v2170, "pMpGJXsPYsFdvxwUYuIXWEWrKxOVodsfafwgFGdAyOkDqbCTjDYjtt");
            }
            else
            {
              printf("GBcLaEbTRJYVvzsOIgK:");
              input_line(&v470, 0x24uLL);
              v475 = ~v475;
              v486 ^= 0x18u;
              v487 ^= 0xC0u;
              v483 ^= 0x6Eu;
              v476 ^= 0x27u;
              v503 ^= 0xC3u;
              v473 ^= 0x7Au;
              v482 ^= 0x5Bu;
              v481 ^= 0x55u;
              v502 ^= 0x6Du;
              v496 ^= 0xF1u;
              v500 ^= 0xEEu;
              v488 ^= 0x58u;
              v498 ^= 0xFEu;
              v505 ^= 0x8Fu;
              v478 ^= 0x13u;
              v485 ^= 0x13u;
              v470 ^= 0xE1u;
              v472 ^= 0x43u;
              v491 ^= 0xC8u;
              v484 ^= 0x56u;
              v499 ^= 0xDEu;
              v474 ^= 0xAFu;
              v497 ^= 0x7Du;
              v495 ^= 0xE1u;
              v477 ^= 0x7Du;
              v501 ^= 0xA4u;
              v489 ^= 0x40u;
              v493 ^= 0xA0u;
              v492 ^= 0x5Au;
              v471 ^= 0x4Eu;
              v504 ^= 0x6Fu;
              v494 ^= 0x7Cu;
              v490 ^= 0x63u;
              v479 ^= 0x18u;
              v480 ^= 0x22u;
              fksth(&v470, "JuxBRtpJWAgAtrgLZmkUtWjcBTCDdJMLwvvA");
            }
            return 0;
          }
          else
          {
            printf("zIvQUethJPgcb:");
            input_line(&v132, 0x21uLL);
            v144 ^= 0xE8u;
            v160 ^= 0x3Fu;
            v133 ^= 0xC3u;
            v137 ^= 0x9Du;
            v149 ^= 0x51u;
            v162 ^= 0xD7u;
            v134 ^= 0xBAu;
            v154 ^= 0xD5u;
            v164 ^= 0xE6u;
            v145 ^= 0xF6u;
            v159 ^= 0x7Fu;
            v140 ^= 0xCEu;
            v158 ^= 0xB8u;
            v156 ^= 0xFDu;
            v148 ^= 0x9Bu;
            v150 ^= 0x16u;
            v143 ^= 0x7Cu;
            v157 ^= 6u;
            v151 ^= 0xC3u;
            v155 ^= 0xE2u;
            v152 ^= 0xB9u;
            v142 ^= 0x7Fu;
            v135 ^= 0x5Du;
            v139 ^= 0xCBu;
            v132 ^= 0xEu;
            v161 ^= 0xB7u;
            v141 ^= 0xFAu;
            v153 ^= 0x15u;
            v138 ^= 0x45u;
            v146 = ~v146;
            v147 ^= 0x13u;
            v136 ^= 0x31u;
            v163 ^= 0xEFu;
            if ( (unsigned int)fksth(&v132, "UOWuQRvdkfmQEXYbrXvtrPHVMaSaeHvjC") )
            {
              printf("KXlsymWPXk:");
              v52 = input_val();
              v53 = input_val();
              v54 = input_val();
              v55 = input_val();
              v56 = input_val();
              v57 = input_val();
              v58 = input_val();
              v59 = input_val();
            }
            else
            {
              printf("IxeaasFAkU:");
              v3287 = input_val();
              v3288 = input_val();
              v3289 = input_val();
              v3290 = input_val();
            }
            return 0;
          }
        }
        else
        {
          printf("WotjZPpAPf:");
          v3322 = input_val();
          v3323 = input_val();
          v3324 = input_val();
          v3325 = input_val();
          if ( v3323 * v3324 == 22294 )
          {
            printf("eLMLZPdiQy:");
            v3315 = input_val();
            v3316 = input_val();
            v3317 = input_val();
            v3318 = input_val();
            v3319 = input_val();
            v3320 = input_val();
            v3321 = input_val();
            if ( v3316 - v3321 == 40516 )
            {
              printf("RLOsCJcTae:");
              v3310 = input_val();
              v3311 = input_val();
              v3312 = input_val();
              v3313 = input_val();
              v3314 = input_val();
            }
            else
            {
              printf("MWDjSMfBeA:");
              v3303 = input_val();
              v3304 = input_val();
              v3305 = input_val();
              v3306 = input_val();
              v3307 = input_val();
              v3308 = input_val();
              v3309 = input_val();
            }
            return 0;
          }
          else
          {
            printf("dBVTofPBceF:");
            input_line(&v796, 0x28uLL);
            v808 ^= 0x5Fu;
            v812 ^= 0xFu;
            v809 ^= 0x76u;
            v802 ^= 0xD9u;
            v798 ^= 0xC4u;
            v831 ^= 0x8Du;
            v799 ^= 0xFEu;
            v811 ^= 0x12u;
            v803 ^= 0xF4u;
            v830 ^= 0x8Bu;
            v828 ^= 0x95u;
            v823 ^= 0x8Cu;
            v824 ^= 0xF1u;
            v800 ^= 0xD5u;
            v819 = ~v819;
            v829 ^= 0xE5u;
            v796 ^= 0xBAu;
            v834 ^= 0x2Eu;
            v801 ^= 0x3Fu;
            v804 ^= 0xBEu;
            v816 ^= 0xEFu;
            v817 ^= 0x2Du;
            v835 ^= 0x8Au;
            v827 ^= 0x2Au;
            v814 ^= 0x80u;
            v813 ^= 3u;
            v825 ^= 0x5Bu;
            v805 ^= 0x1Fu;
            v818 ^= 0xE3u;
            v806 ^= 0x49u;
            v833 ^= 0x8Bu;
            v826 ^= 0xBFu;
            v797 ^= 8u;
            v807 ^= 0xCCu;
            v822 ^= 0xCAu;
            v821 ^= 0x5Du;
            v815 ^= 0x58u;
            v832 ^= 0x98u;
            v810 ^= 0x64u;
            v820 ^= 0x3Du;
            if ( (unsigned int)fksth(&v796, "lbIjndZBuuNRKRcyyjooDrBGRoihYMqTosnqXljn") )
            {
              printf("SFDwulNhyk:");
              v3291 = input_val();
              v3292 = input_val();
              v3293 = input_val();
              v3294 = input_val();
              v3295 = input_val();
              v3296 = input_val();
              v3297 = input_val();
            }
            else
            {
              printf("ADDelghkzQ:");
              v3298 = input_val();
              v3299 = input_val();
              v3300 = input_val();
              v3301 = input_val();
              v3302 = input_val();
            }
            return 0;
          }
        }
      }
    }
    else
    {
      printf("gyhnSHTkjUVc:");
      input_line(&v506, 0x24uLL);
      v531 ^= 0x2Cu;
      v515 ^= 0x35u;
      v511 ^= 0x3Du;
      v533 ^= 0xA2u;
      v534 ^= 0x3Du;
      v525 ^= 0xC5u;
      v537 ^= 0x29u;
      v540 ^= 0x5Fu;
      v508 ^= 0x1Bu;
      v536 ^= 0x8Eu;
      v529 ^= 0x39u;
      v516 ^= 0xB5u;
      v538 ^= 0xF6u;
      v506 ^= 0x7Bu;
      v521 ^= 0x6Eu;
      v524 ^= 0x47u;
      v519 ^= 0x87u;
      v532 ^= 0x7Fu;
      v522 ^= 0x23u;
      v530 ^= 0x8Fu;
      v513 ^= 0x27u;
      v514 ^= 0xACu;
      v509 ^= 0xE8u;
      v517 ^= 4u;
      v528 ^= 0x58u;
      v527 ^= 0x32u;
      v510 ^= 0x56u;
      v539 ^= 0xD9u;
      v526 ^= 0x5Du;
      v535 ^= 0x7Du;
      v541 ^= 0xE9u;
      v518 ^= 0x8Au;
      v523 ^= 0xB7u;
      v520 ^= 0x13u;
      v512 ^= 0xFEu;
      v507 ^= 0x37u;
      if ( (unsigned int)fksth(&v506, "SiKBAvXAKiUZVbJVEJhzyqdYxwdCouNVPDVR") )
      {
        printf("xZEikgeuVW:");
        v3192 = input_val();
        v3193 = input_val();
        v3194 = input_val();
        v3195 = input_val();
        v3196 = input_val();
        v3197 = input_val();
        if ( v3193 * v3192 - v3196 == 23585 )
        {
          printf("SqGHlHVBVwQinWaQi:");
          input_line(&v836, 0x29uLL);
          v856 ^= 0xB6u;
          v850 ^= 0x45u;
          v861 ^= 0xF7u;
          v840 ^= 0x99u;
          v843 ^= 0xDu;
          v858 ^= 0x38u;
          v849 ^= 0xBDu;
          v860 ^= 0x64u;
          v853 ^= 0xEu;
          v862 ^= 0xF0u;
          v867 ^= 0xDEu;
          v842 ^= 0x4Cu;
          v859 ^= 0xCBu;
          v854 ^= 0x83u;
          v841 ^= 0x8Cu;
          v836 ^= 0x28u;
          v872 ^= 0x95u;
          v855 ^= 0x5Au;
          v857 ^= 0x73u;
          v846 ^= 0xB7u;
          v845 ^= 0x78u;
          v847 ^= 0xDFu;
          v874 ^= 0xE0u;
          v851 ^= 7u;
          v868 ^= 0x5Au;
          v837 ^= 0xD9u;
          v852 ^= 0x9Cu;
          v865 ^= 0x6Cu;
          v875 ^= 0x94u;
          v873 ^= 0x19u;
          v848 ^= 0x18u;
          v866 ^= 0xD5u;
          v876 ^= 0x36u;
          v870 ^= 0x22u;
          v871 ^= 0x52u;
          v869 ^= 0xC4u;
          v839 ^= 0xCu;
          v838 ^= 0xF2u;
          v863 ^= 0x57u;
          v844 ^= 0x80u;
          v864 ^= 0xCFu;
          if ( (unsigned int)fksth(&v836, "ExsEQrZmjlXmFynPiCzPEIhxbrwVGdrQxEghmqAKS") )
          {
            printf("XbIBrPhICRHoxdBcbZ:");
            input_line(&v614, 0x25uLL);
            v616 ^= 0xAAu;
            v620 ^= 0x2Fu;
            v628 ^= 0x47u;
            v621 ^= 0x6Fu;
            v644 ^= 0x75u;
            v641 ^= 0x9Fu;
            v630 ^= 0xEAu;
            v631 ^= 0xB4u;
            v643 ^= 0xC5u;
            v635 ^= 0xF0u;
            v636 ^= 0xA9u;
            v649 ^= 0xDBu;
            v622 ^= 0xD5u;
            v639 ^= 0xBAu;
            v645 ^= 0xB8u;
            v633 ^= 0xD5u;
            v626 ^= 0xE8u;
            v624 ^= 8u;
            v646 ^= 0xF5u;
            v625 ^= 0x26u;
            v650 ^= 0xA0u;
            v642 ^= 0x5Fu;
            v648 ^= 0xB0u;
            v640 ^= 0xF2u;
            v634 ^= 0x20u;
            v637 ^= 0xCu;
            v638 ^= 0x49u;
            v617 ^= 0x62u;
            v614 ^= 0x84u;
            v619 ^= 0x53u;
            v627 ^= 0x4Eu;
            v647 ^= 0x6Bu;
            v629 ^= 0xA1u;
            v632 ^= 6u;
            v618 ^= 0x47u;
            v615 ^= 0x47u;
            v623 ^= 0xD3u;
            if ( (unsigned int)fksth(&v614, "sLMLmrRxJFMiJNMueIWZSFObRvKKVhIvrURpG") )
            {
              printf("pShLkuBCTgpfMYJf:");
              input_line(&v1964, 0x33uLL);
              v1992 ^= 0x4Du;
              v2012 ^= 0x67u;
              v1988 ^= 0xA9u;
              v1965 ^= 0x4Au;
              v1995 ^= 0xD5u;
              v2013 ^= 0x45u;
              v2011 ^= 0xE3u;
              v1974 ^= 0xF2u;
              v1996 ^= 0xACu;
              v1969 ^= 0x13u;
              v1976 ^= 0x1Fu;
              v1989 ^= 0xF7u;
              v1984 ^= 0xEEu;
              v2001 ^= 0xF2u;
              v1977 ^= 0x81u;
              v1967 ^= 0xB0u;
              v2005 = ~v2005;
              v2006 ^= 0xD8u;
              v1981 ^= 0xC2u;
              v1970 ^= 0xEDu;
              v1973 ^= 0x1Eu;
              v2004 ^= 0x7Bu;
              v1994 ^= 0x1Eu;
              v1975 ^= 0xABu;
              v2014 ^= 0xB7u;
              v1979 ^= 0xBCu;
              v2009 ^= 0x7Cu;
              v1987 ^= 0xF5u;
              v1998 ^= 0x6Bu;
              v1966 ^= 0xE7u;
              v2003 ^= 0x2Cu;
              v2010 ^= 0x8Bu;
              v2002 ^= 0x15u;
              v2008 ^= 0x80u;
              v1997 ^= 0x16u;
              v1982 ^= 0xABu;
              v1999 ^= 0x31u;
              v2007 ^= 0x85u;
              v1971 ^= 0x57u;
              v1964 ^= 0xF2u;
              v1968 ^= 0xF1u;
              v1993 ^= 0x66u;
              v1983 ^= 0x1Du;
              v1972 ^= 0xE7u;
              v1991 ^= 0xBDu;
              v1986 ^= 0x1Au;
              v1985 ^= 0x39u;
              v1980 ^= 0x10u;
              v1990 ^= 0x55u;
              v2000 ^= 0x38u;
              v1978 ^= 0xAAu;
              fksth(&v1964, "xOSLIhmUiXXfkPAuoRRlTAxjNLSzyrAtsqvdxQEsXJVqsHfsPpn");
            }
            else
            {
              printf("JztsBVGolW:");
              v3158 = input_val();
              v3159 = input_val();
              v3160 = input_val();
              v3161 = input_val();
            }
            return 0;
          }
          else
          {
            printf("gvEQRwDcGecLgPGLXC:");
            input_line(&v2279, 0x38uLL);
            v2327 ^= 0xF4u;
            v2319 ^= 0xE9u;
            v2318 ^= 0x69u;
            v2310 ^= 0x33u;
            v2284 ^= 0xEAu;
            v2315 ^= 0x25u;
            v2294 ^= 0xC0u;
            v2334 ^= 0x26u;
            v2302 ^= 0xC4u;
            v2324 ^= 0x73u;
            v2300 ^= 0xB2u;
            v2303 ^= 0x73u;
            v2329 ^= 0xDBu;
            v2332 ^= 0x79u;
            v2285 ^= 0x29u;
            v2308 ^= 0x3Bu;
            v2295 ^= 0xD8u;
            v2298 ^= 0xD4u;
            v2307 ^= 0xFAu;
            v2311 ^= 0x3Eu;
            v2282 ^= 0x59u;
            v2316 ^= 0xDEu;
            v2301 ^= 0x69u;
            v2305 ^= 0x9Eu;
            v2331 ^= 0x5Fu;
            v2309 ^= 0x4Bu;
            v2326 ^= 0x93u;
            v2297 ^= 0x49u;
            v2313 ^= 0x35u;
            v2330 ^= 0xA6u;
            v2291 ^= 0xC3u;
            v2321 ^= 0x89u;
            v2299 ^= 0xCEu;
            v2283 ^= 0xEDu;
            v2290 ^= 7u;
            v2312 ^= 0xAEu;
            v2287 ^= 0xC7u;
            v2304 ^= 1u;
            v2328 ^= 0x1Cu;
            v2322 ^= 0x43u;
            v2320 ^= 0x38u;
            v2280 ^= 0xCu;
            v2286 ^= 0x60u;
            v2281 ^= 0x6Cu;
            v2314 ^= 0xBCu;
            v2323 ^= 0xA4u;
            v2292 ^= 0x77u;
            v2306 ^= 0xE6u;
            v2333 ^= 0x3Eu;
            v2325 ^= 0x9Cu;
            v2317 ^= 0xC2u;
            v2289 ^= 0x19u;
            v2296 ^= 0xE0u;
            v2288 ^= 0x6Bu;
            v2293 ^= 0x3Du;
            if ( (unsigned int)fksth(&v2279, "DIbwMSaunVIKLTyBEMyYnRughbJsrgSpsetmKiNWPRajwDwRglZwRamF") )
            {
              printf("wyQYLAmPQwwCCMkhm:");
              input_line(&v2682, 0x3BuLL);
              v2720 ^= 0xB3u;
              v2725 ^= 0xCu;
              v2710 ^= 0xA6u;
              v2713 ^= 0xFDu;
              v2685 ^= 0xAEu;
              v2715 ^= 0x34u;
              v2711 ^= 0x46u;
              v2729 ^= 0xA1u;
              v2716 ^= 0xC1u;
              v2738 ^= 0x66u;
              v2735 ^= 0x7Bu;
              v2687 ^= 0x68u;
              v2723 ^= 0x83u;
              v2708 ^= 0xC3u;
              v2737 ^= 0xE6u;
              v2705 ^= 0xBDu;
              v2730 ^= 0x44u;
              v2707 ^= 0xA1u;
              v2721 ^= 0x42u;
              v2688 ^= 0xD1u;
              v2718 ^= 0x61u;
              v2709 ^= 0xA3u;
              v2727 ^= 0x69u;
              v2733 ^= 0x8Bu;
              v2701 ^= 0xCEu;
              v2726 ^= 0x1Fu;
              v2686 ^= 0x30u;
              v2712 ^= 0x80u;
              v2724 ^= 0xACu;
              v2732 ^= 0x74u;
              v2683 ^= 0x63u;
              v2703 ^= 0x52u;
              v2690 ^= 0xACu;
              v2699 ^= 0xB7u;
              v2695 ^= 0x9Fu;
              v2696 ^= 0xCCu;
              v2693 ^= 0xC1u;
              v2691 ^= 0x43u;
              v2698 ^= 0x7Du;
              v2719 ^= 0x88u;
              v2728 ^= 0x2Au;
              v2700 ^= 0x36u;
              v2697 ^= 0xE1u;
              v2717 ^= 0x4Cu;
              v2689 ^= 3u;
              v2739 ^= 0x70u;
              v2682 ^= 0x8Du;
              v2740 ^= 0xC6u;
              v2722 ^= 0xA5u;
              v2704 ^= 0x24u;
              v2702 ^= 0xFEu;
              v2694 ^= 0x40u;
              v2692 ^= 0xBEu;
              v2714 ^= 0x46u;
              v2706 ^= 0xF7u;
              v2731 ^= 0xCDu;
              v2734 ^= 6u;
              v2736 ^= 0x64u;
              v2684 ^= 0xB5u;
              fksth(&v2682, "yDLKpakBAixTKKPzrhlOWJZGJhLqNlUzqiXKIVIVhgksvLZoXqgbvbCGnTF");
            }
            else
            {
              printf("AflFKAQhZiqhYXYksWN:");
              input_line(&v3162, 0x1EuLL);
              v3183 ^= 0x69u;
              v3179 ^= 0x32u;
              v3180 ^= 0x76u;
              v3176 ^= 0x76u;
              v3166 ^= 0x1Du;
              v3189 ^= 0xD4u;
              v3182 ^= 0x35u;
              v3187 ^= 0x67u;
              v3163 ^= 0xE1u;
              v3172 ^= 0xD8u;
              v3168 ^= 0x9Du;
              v3170 ^= 0x67u;
              v3173 ^= 0x92u;
              v3167 ^= 0x2Au;
              v3165 ^= 0x82u;
              v3169 ^= 0xCCu;
              v3171 ^= 0xE4u;
              v3188 ^= 0x55u;
              v3184 ^= 0xB8u;
              v3177 ^= 0x44u;
              v3164 ^= 0xE1u;
              v3186 ^= 0x3Du;
              v3181 ^= 0x4Du;
              v3162 ^= 0x5Cu;
              v3191 ^= 0x44u;
              v3190 ^= 0x8Fu;
              v3178 ^= 0xADu;
              v3185 ^= 0xC3u;
              v3175 ^= 0x35u;
              v3174 ^= 0x2Cu;
              fksth(&v3162, "jCdwXWNrehdkkdTBgKLTJCCKheIOoX");
            }
            return 0;
          }
        }
        else
        {
          printf("TbWkXilXUGHzmwMT:");
          input_line(&v231, 0x22uLL);
          v232 ^= 0x77u;
          v260 ^= 0x57u;
          v238 ^= 0xEBu;
          v262 ^= 0xA0u;
          v236 ^= 0xCCu;
          v242 ^= 0xBEu;
          v234 ^= 0x93u;
          v257 ^= 0xE3u;
          v256 ^= 0x1Du;
          v233 ^= 0x4Du;
          v249 ^= 0x61u;
          v239 ^= 0xD8u;
          v250 ^= 0x2Cu;
          v243 ^= 0xE8u;
          v246 ^= 0x56u;
          v251 ^= 0x90u;
          v264 ^= 0xF4u;
          v263 ^= 0x35u;
          v254 ^= 0xD4u;
          v253 ^= 0xDEu;
          v237 ^= 0xF5u;
          v247 ^= 0xF7u;
          v235 ^= 0x3Fu;
          v255 ^= 0x6Eu;
          v252 ^= 0x74u;
          v241 ^= 0xCu;
          v240 ^= 0x6Bu;
          v248 ^= 0xFEu;
          v259 ^= 0x1Au;
          v261 ^= 0x1Au;
          v231 ^= 8u;
          v245 ^= 0xF8u;
          v244 ^= 0x23u;
          v258 ^= 0xCBu;
          if ( (unsigned int)fksth(&v231, "kwntTnJKiKZsrsuSHsNtfBGeLyTHrCNhcM") )
          {
            printf("gieFTorSQJ:");
            v3139 = input_val();
            v3140 = input_val();
            v3141 = input_val();
            v3142 = input_val();
            v3143 = input_val();
            v3144 = input_val();
            v3145 = input_val();
            if ( v3139 + v3141 == 37802 )
            {
              printf("raaMjKGfqA:");
              v3132 = input_val();
              v3133 = input_val();
              v3134 = input_val();
              v3135 = input_val();
              v3136 = input_val();
              v3137 = input_val();
              v3138 = input_val();
            }
            else
            {
              printf("amSETrMyHW:");
              v3128 = input_val();
              v3129 = input_val();
              v3130 = input_val();
              v3131 = input_val();
            }
            return 0;
          }
          else
          {
            printf("iwVeLgIfJnsk:");
            input_line(&v918, 0x2AuLL);
            v922 ^= 0x21u;
            v952 ^= 0x8Bu;
            v951 ^= 0xD6u;
            v946 ^= 0xA4u;
            v934 ^= 0xA4u;
            v944 ^= 0x18u;
            v957 ^= 0x60u;
            v935 ^= 0x89u;
            v925 ^= 0x2Au;
            v949 ^= 0x1Fu;
            v918 ^= 0x7Eu;
            v939 ^= 0x4Bu;
            v920 ^= 0xADu;
            v941 ^= 0x87u;
            v955 ^= 0xBEu;
            v921 ^= 0xF2u;
            v950 ^= 0x2Au;
            v958 ^= 0x47u;
            v938 ^= 0x93u;
            v929 ^= 0xD4u;
            v933 ^= 0x7Du;
            v932 ^= 0x7Bu;
            v937 ^= 0x94u;
            v943 ^= 0x8Au;
            v930 ^= 0x8Cu;
            v931 ^= 0x88u;
            v956 ^= 0xDCu;
            v959 ^= 0x42u;
            v924 ^= 0x19u;
            v947 ^= 0x65u;
            v940 ^= 0x8Fu;
            v923 ^= 0x33u;
            v936 ^= 0xAAu;
            v927 ^= 0xBu;
            v945 ^= 0xD7u;
            v953 ^= 0x4Au;
            v948 ^= 0xF4u;
            v919 ^= 0x4Bu;
            v926 ^= 0xCCu;
            v954 ^= 0x19u;
            v942 ^= 0xE9u;
            v928 ^= 0x41u;
            if ( (unsigned int)fksth(&v918, "XqqOaYWkMtTSOUtpdkpTPnELplEpIhMIMtnueIJVRl") )
            {
              printf("KJrvjIBSPF:");
              v3146 = input_val();
              v3147 = input_val();
              v3148 = input_val();
              v3149 = input_val();
              v3150 = input_val();
              v3151 = input_val();
              v3152 = input_val();
            }
            else
            {
              printf("bEjdeHxaWd:");
              v3153 = input_val();
              v3154 = input_val();
              v3155 = input_val();
              v3156 = input_val();
              v3157 = input_val();
            }
            return 0;
          }
        }
      }
      else
      {
        printf("psYdsPJuBdjYysk:");
        input_line(&v1866, 0x32uLL);
        v1889 ^= 0xA6u;
        v1884 ^= 0xA8u;
        v1867 ^= 0x52u;
        v1892 ^= 0x7Cu;
        v1899 ^= 0xE4u;
        v1882 ^= 0xAFu;
        v1901 ^= 0xB9u;
        v1875 ^= 0x76u;
        v1896 ^= 0x53u;
        v1911 ^= 0x50u;
        v1908 ^= 0xD6u;
        v1880 ^= 0xB9u;
        v1881 ^= 0x5Au;
        v1877 ^= 0x40u;
        v1902 ^= 6u;
        v1870 ^= 0x93u;
        v1910 ^= 0xB4u;
        v1914 ^= 0x98u;
        v1897 ^= 0x42u;
        v1886 ^= 0x76u;
        v1904 ^= 0x88u;
        v1876 ^= 0x74u;
        v1866 ^= 0x3Cu;
        v1883 ^= 0x9Fu;
        v1907 ^= 0x53u;
        v1893 ^= 0x1Eu;
        v1912 ^= 0x4Du;
        v1890 ^= 0x37u;
        v1906 ^= 0xEBu;
        v1909 ^= 0x2Fu;
        v1872 ^= 0x58u;
        v1888 ^= 0x97u;
        v1903 ^= 0xAu;
        v1869 ^= 0x7Eu;
        v1891 ^= 0x17u;
        v1887 ^= 0x20u;
        v1900 ^= 0x3Au;
        v1874 ^= 0xEAu;
        v1895 ^= 0x9Au;
        v1879 ^= 0x7Cu;
        v1913 ^= 0x6Eu;
        v1905 ^= 0xB1u;
        v1878 ^= 0xE0u;
        v1873 ^= 0xBBu;
        v1868 ^= 0x42u;
        v1898 ^= 0xE8u;
        v1885 ^= 0x2Cu;
        v1915 ^= 0x96u;
        v1871 ^= 0xEEu;
        v1894 ^= 0x4Bu;
        if ( (unsigned int)fksth(&v1866, "YmHwuuoTOyPpmcjwgGeOafzAaVGzZviErEqBTTocOdXNheHAEd") )
        {
          printf("SIKPifIuQbzHWNnXkL:");
          input_line(&v3214, 0x1FuLL);
          v3214 ^= 2u;
          v3215 ^= 0xD6u;
          v3232 ^= 0xEBu;
          v3235 ^= 0xFCu;
          v3244 ^= 0xB3u;
          v3221 ^= 0x80u;
          v3220 ^= 0x84u;
          v3226 ^= 0x3Cu;
          v3241 ^= 0x3Fu;
          v3237 ^= 0x85u;
          v3216 ^= 0x9Du;
          v3243 ^= 8u;
          v3231 ^= 0x31u;
          v3238 ^= 0x6Bu;
          v3240 ^= 0x84u;
          v3233 ^= 5u;
          v3225 ^= 0x78u;
          v3217 ^= 0xBFu;
          v3242 ^= 0x23u;
          v3239 ^= 0xD2u;
          v3228 ^= 0x97u;
          v3219 ^= 0x46u;
          v3229 ^= 0xB9u;
          v3222 ^= 0x6Eu;
          v3230 ^= 0x5Cu;
          v3234 ^= 0xE4u;
          v3218 ^= 0xBDu;
          v3224 ^= 0x4Du;
          v3223 ^= 0x8Eu;
          v3227 ^= 0x31u;
          v3236 ^= 0x65u;
          if ( (unsigned int)fksth(&v3214, "CJFWwPkeHTKOWgGeFsTlDqlEhhBpCEb") )
          {
            printf("KdrlZDeJrk:");
            v3202 = input_val();
            v3203 = input_val();
            v3204 = input_val();
            v3205 = input_val();
            v3206 = input_val();
            v3207 = input_val();
            if ( ((v3204 - v3206) ^ v3207) == 41625 )
            {
              printf("iWMXkiaFPsidsuthJEmr:");
              input_line(&v1485, 0x2EuLL);
              v1529 ^= 0x30u;
              v1511 ^= 0xB6u;
              v1515 ^= 0x27u;
              v1505 ^= 0xF7u;
              v1503 ^= 0xBAu;
              v1501 ^= 0xCEu;
              v1524 ^= 6u;
              v1507 ^= 5u;
              v1525 ^= 0xA6u;
              v1506 ^= 0xC8u;
              v1500 ^= 0xF4u;
              v1493 ^= 0x24u;
              v1512 ^= 0x70u;
              v1494 ^= 0xCDu;
              v1530 ^= 0xF3u;
              v1518 ^= 0x48u;
              v1520 ^= 0x88u;
              v1490 ^= 0xDAu;
              v1491 ^= 0x17u;
              v1508 ^= 0xE7u;
              v1521 ^= 0xFu;
              v1516 ^= 0xF2u;
              v1504 ^= 0xCFu;
              v1486 ^= 0x90u;
              v1510 ^= 0x69u;
              v1488 ^= 0x10u;
              v1522 ^= 0x3Eu;
              v1496 ^= 0xF2u;
              v1526 ^= 0x4Du;
              v1523 ^= 0xEBu;
              v1519 ^= 0x2Du;
              v1485 ^= 0xCDu;
              v1498 ^= 0xE5u;
              v1489 ^= 0xABu;
              v1527 ^= 0x4Du;
              v1497 ^= 0x89u;
              v1514 ^= 6u;
              v1528 ^= 0xACu;
              v1499 ^= 0xE4u;
              v1502 ^= 0x5Eu;
              v1517 ^= 0x79u;
              v1492 ^= 0xFu;
              v1495 ^= 0xEAu;
              v1513 ^= 0x43u;
              v1487 ^= 0xA1u;
              v1509 ^= 0x9Bu;
              fksth(&v1485, "GMarLvmuibNNrDztySyGOnkdjbxnqUwWPteZNWwMSjxXsp");
            }
            else
            {
              printf("nMqKtGByuL:");
              v3198 = input_val();
              v3199 = input_val();
              v3200 = input_val();
              v3201 = input_val();
            }
            return 0;
          }
          else
          {
            printf("iYiWznLSFtc:");
            input_line(&v1305, 0x2DuLL);
            v1342 ^= 0x59u;
            v1322 ^= 0x41u;
            v1336 ^= 0xEDu;
            v1327 ^= 0x7Au;
            v1332 ^= 0xC0u;
            v1319 ^= 0xFCu;
            v1340 ^= 0x1Fu;
            v1324 ^= 0xB2u;
            v1326 ^= 0x4Du;
            v1333 ^= 0x54u;
            v1315 ^= 0xB7u;
            v1312 ^= 0xAAu;
            v1347 ^= 0x72u;
            v1349 ^= 0x5Cu;
            v1328 ^= 2u;
            v1331 ^= 0x58u;
            v1325 ^= 0x97u;
            v1320 ^= 0x35u;
            v1321 ^= 0xFEu;
            v1318 ^= 0xA5u;
            v1343 ^= 0xB3u;
            v1338 ^= 0x21u;
            v1311 ^= 0x71u;
            v1316 ^= 0xBCu;
            v1341 ^= 0xBAu;
            v1329 ^= 0xBCu;
            v1310 ^= 0x3Cu;
            v1330 ^= 0x52u;
            v1313 ^= 0x82u;
            v1346 = ~v1346;
            v1306 ^= 0xD8u;
            v1345 ^= 0xCCu;
            v1308 ^= 0x83u;
            v1335 ^= 0x1Eu;
            v1307 ^= 0x5Fu;
            v1348 ^= 0xBCu;
            v1334 ^= 0x17u;
            v1314 ^= 0x5Eu;
            v1339 ^= 0x9Du;
            v1309 ^= 0x83u;
            v1337 ^= 0x12u;
            v1323 ^= 0xC8u;
            v1317 ^= 0x2Du;
            v1344 ^= 0xB1u;
            v1305 ^= 0x3Au;
            if ( (unsigned int)fksth(&v1305, "uowwMSsGnKqHlfYdwxtJloQfGddlyUvNgrNdISESZWkfm") )
            {
              printf("TZxinMQgZRPIqTHLcn:");
              input_line(&v60, 0x20uLL);
              v80 ^= 0x4Bu;
              v64 ^= 0x45u;
              v60 = ~v60;
              v74 ^= 0x44u;
              v71 ^= 0x63u;
              v70 ^= 0x16u;
              v79 ^= 0x99u;
              v82 ^= 0x37u;
              v62 ^= 0x59u;
              v90 ^= 0x4Cu;
              v63 ^= 0x5Cu;
              v83 ^= 0x71u;
              v86 ^= 0x44u;
              v67 ^= 0x4Eu;
              v75 ^= 0x6Cu;
              v87 ^= 0xF9u;
              v84 ^= 0xB0u;
              v88 ^= 0x63u;
              v78 ^= 0x8Fu;
              v73 ^= 0x6Eu;
              v68 ^= 0xA0u;
              v65 ^= 0x15u;
              v69 ^= 0x39u;
              v72 ^= 0xF1u;
              v61 ^= 4u;
              v76 ^= 0xADu;
              v85 ^= 0xAAu;
              v66 ^= 0xC7u;
              v89 ^= 0x54u;
              v77 ^= 0x72u;
              v91 ^= 0xF3u;
              v81 ^= 0x2Bu;
              fksth(&v60, "ZUyKlrUruVsrZYiRXKkApsUXRMkbGzQU");
            }
            else
            {
              printf("HhXRUNPKYx:");
              v3208 = input_val();
              v3209 = input_val();
              v3210 = input_val();
              v3211 = input_val();
              v3212 = input_val();
              v3213 = input_val();
            }
            return 0;
          }
        }
        else
        {
          printf("jsstdzecUn:");
          v3282 = input_val();
          v3283 = input_val();
          v3284 = input_val();
          v3285 = input_val();
          v3286 = input_val();
          if ( v3284 * v3285 == 23988 )
          {
            printf("NOWmUuytrDEFYwDupS:");
            input_line(&v1218, 0x2CuLL);
            v1248 ^= 0x32u;
            v1223 ^= 0x8Du;
            v1257 ^= 0xF4u;
            v1233 ^= 0x99u;
            v1260 ^= 0x4Fu;
            v1252 ^= 0x82u;
            v1228 ^= 0xE0u;
            v1243 ^= 0xF0u;
            v1235 ^= 0x8Au;
            v1225 ^= 0xFDu;
            v1224 ^= 0xDEu;
            v1242 ^= 0x97u;
            v1244 ^= 0x84u;
            v1245 ^= 0x69u;
            v1229 ^= 3u;
            v1219 ^= 0x18u;
            v1250 ^= 0x9Cu;
            v1238 ^= 0xB7u;
            v1241 ^= 0x50u;
            v1240 ^= 0x20u;
            v1226 ^= 0x8Eu;
            v1253 ^= 0xC6u;
            v1256 ^= 0x8Fu;
            v1251 ^= 0x78u;
            v1239 ^= 0x38u;
            v1247 ^= 0x32u;
            v1221 ^= 0xECu;
            v1255 ^= 0x31u;
            v1249 ^= 0x26u;
            v1259 ^= 0x42u;
            v1254 ^= 0xCBu;
            v1246 ^= 0x1Fu;
            v1232 ^= 0xDu;
            v1227 ^= 0x37u;
            v1258 ^= 0x44u;
            v1230 ^= 0x8Bu;
            v1231 ^= 0x11u;
            v1236 ^= 0x48u;
            v1222 ^= 0x19u;
            v1220 ^= 0xDBu;
            v1237 ^= 0x5Du;
            v1218 ^= 0x8Du;
            v1234 ^= 0x79u;
            if ( (unsigned int)fksth(&v1218, "VJPUsAFGlduBqpZDKRbpqkSsauKbNkgaMsQTKSGgHrnl") )
            {
              printf("XKguOrTvCZeS:");
              input_line(&v3251, 0x1FuLL);
              v3255 ^= 0x11u;
              v3271 ^= 0x90u;
              v3272 ^= 0x8Cu;
              v3277 ^= 0xC7u;
              v3274 ^= 0xDEu;
              v3261 ^= 0x4Eu;
              v3268 ^= 0xA8u;
              v3269 ^= 0xE4u;
              v3273 ^= 0x48u;
              v3281 ^= 0x30u;
              v3254 ^= 0xAu;
              v3253 ^= 0x46u;
              v3263 ^= 0x6Eu;
              v3267 ^= 0xA6u;
              v3251 ^= 0x5Eu;
              v3262 ^= 0x37u;
              v3265 ^= 0x69u;
              v3275 ^= 0xE0u;
              v3280 ^= 0x29u;
              v3266 ^= 0xA3u;
              v3257 ^= 0x79u;
              v3276 ^= 0xB6u;
              v3270 ^= 0x4Bu;
              v3259 ^= 0x2Du;
              v3256 ^= 0xB6u;
              v3264 ^= 0xCDu;
              v3252 ^= 0x43u;
              v3279 ^= 0xB7u;
              v3258 ^= 0x31u;
              v3278 ^= 0x55u;
              v3260 ^= 0xBu;
              fksth(&v3251, "JMHMXjMqByTsoxTDOdBmURxzupxvHOS");
            }
            else
            {
              printf("HsFvHgOhGKYfxTMl:");
              input_line(&v2015, 0x34uLL);
              v2038 ^= 0x6Eu;
              v2063 ^= 0x2Bu;
              v2058 ^= 0x10u;
              v2030 ^= 0xA3u;
              v2025 ^= 0x77u;
              v2034 ^= 0xA6u;
              v2027 ^= 0x5Eu;
              v2031 ^= 0xC8u;
              v2049 ^= 0x70u;
              v2048 ^= 0xA0u;
              v2015 ^= 0xB1u;
              v2042 ^= 0xD7u;
              v2051 ^= 0x65u;
              v2040 ^= 0xBDu;
              v2046 ^= 0xC2u;
              v2028 ^= 0xD1u;
              v2035 ^= 0x8Cu;
              v2036 ^= 0xB6u;
              v2043 ^= 0x8Du;
              v2024 ^= 0x1Au;
              v2047 ^= 0x16u;
              v2033 ^= 0xD6u;
              v2029 ^= 0x83u;
              v2016 ^= 0x46u;
              v2044 ^= 0xDDu;
              v2021 ^= 0x8Eu;
              v2023 ^= 0xFAu;
              v2055 ^= 0x81u;
              v2065 ^= 0x97u;
              v2061 ^= 0xFAu;
              v2022 ^= 0xC6u;
              v2062 ^= 0x5Du;
              v2026 ^= 0x91u;
              v2054 ^= 0xD2u;
              v2019 ^= 0x45u;
              v2032 ^= 0xB8u;
              v2045 ^= 0xC0u;
              v2039 ^= 0xA7u;
              v2017 ^= 0xB6u;
              v2053 ^= 0x64u;
              v2037 ^= 0x34u;
              v2020 ^= 0x77u;
              v2056 ^= 0xB0u;
              v2059 ^= 0x6Bu;
              v2052 ^= 0xE6u;
              v2018 ^= 0x2Bu;
              v2057 ^= 0xB0u;
              v2041 ^= 0x7Bu;
              v2064 ^= 0x39u;
              v2060 ^= 0xCDu;
              v2050 ^= 0x6Bu;
              fksth(&v2015, "gYIguAnHOOkmRSlmfGBOkVFELmMcdfcsYGYkzIetopyQyxsICHSq");
            }
            return 0;
          }
          else
          {
            printf("suqQnHckLVqPA:");
            input_line(&v435, 0x23uLL);
            v438 ^= 0x53u;
            v458 ^= 0xEBu;
            v439 ^= 0x26u;
            v435 ^= 0x69u;
            v445 = ~v445;
            v448 ^= 0x7Fu;
            v461 ^= 0x6Cu;
            v467 ^= 0xFBu;
            v437 ^= 0xA8u;
            v463 ^= 0xC1u;
            v462 ^= 0xB7u;
            v452 ^= 0x71u;
            v459 ^= 0x46u;
            v456 ^= 0x69u;
            v464 ^= 0x40u;
            v447 ^= 0x7Bu;
            v440 ^= 0xCEu;
            v443 ^= 0x49u;
            v451 ^= 0xABu;
            v453 ^= 0xE0u;
            v446 ^= 0xCFu;
            v460 ^= 0xCCu;
            v469 ^= 0x55u;
            v449 ^= 0x97u;
            v444 ^= 0xAFu;
            v457 ^= 0xD4u;
            v441 ^= 0x8Bu;
            v468 ^= 0x19u;
            v454 ^= 0xC9u;
            v442 ^= 0x95u;
            v436 ^= 0x97u;
            v465 ^= 0xEBu;
            v450 ^= 0xBBu;
            v466 ^= 0x1Au;
            v455 ^= 0x8Cu;
            if ( (unsigned int)fksth(&v435, "WAKOMsoaErXWthVCwDRgoYBRzPnHzQDxjTZ") )
            {
              printf("MuuFTjCwsb:");
              v3245 = input_val();
              v3246 = input_val();
              v3247 = input_val();
              v3248 = input_val();
              v3249 = input_val();
              v3250 = input_val();
            }
            else
            {
              printf("TmlQucGUTygPIrVfC:");
              input_line(&v688, 0x26uLL);
              v716 ^= 0xAFu;
              v701 ^= 0xE4u;
              v718 ^= 0x8Eu;
              v722 ^= 0xF7u;
              v709 ^= 0x6Du;
              v723 ^= 0xF1u;
              v720 ^= 0x89u;
              v724 ^= 0x83u;
              v725 ^= 0x27u;
              v719 ^= 0x7Fu;
              v691 ^= 0x19u;
              v717 ^= 0xABu;
              v721 ^= 0xF2u;
              v707 ^= 0xC1u;
              v705 ^= 0x77u;
              v712 ^= 0xFDu;
              v700 ^= 0xAEu;
              v713 ^= 0xBCu;
              v694 ^= 0x65u;
              v696 ^= 0xB6u;
              v693 ^= 5u;
              v702 ^= 0x60u;
              v708 ^= 0x5Cu;
              v714 ^= 0x10u;
              v698 ^= 0x61u;
              v704 ^= 0x12u;
              v711 ^= 0x58u;
              v692 ^= 0x49u;
              v689 ^= 0xB8u;
              v697 ^= 0xA0u;
              v703 ^= 0xC7u;
              v699 ^= 0xEAu;
              v715 ^= 0xE0u;
              v706 ^= 0xD3u;
              v710 ^= 0xF7u;
              v688 ^= 0x37u;
              v690 ^= 0xCBu;
              v695 ^= 0x39u;
              fksth(&v688, "kfVNjijFXhgojJuOmUIaNiWoPhWppfMUqkWIsI");
            }
            return 0;
          }
        }
      }
    }
  }
}```


After
```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  char v4[46]; // [rsp+740h] [rbp-D60h] BYREF
  char v5[51]; // [rsp+9C0h] [rbp-AE0h] BYREF
  char v6[53]; // [rsp+AC0h] [rbp-9E0h] BYREF
  char v7[59]; // [rsp+C40h] [rbp-860h] BYREF
  char v8[109]; // [rsp+E00h] [rbp-6A0h] BYREF
  int v9; // [rsp+E80h] [rbp-620h]
  int v10; // [rsp+E84h] [rbp-61Ch]
  int v11; // [rsp+E88h] [rbp-618h]
  int v12; // [rsp+E8Ch] [rbp-614h]
  int v13; // [rsp+E90h] [rbp-610h]
  int v14; // [rsp+EA0h] [rbp-600h]
  int v15; // [rsp+EA4h] [rbp-5FCh]
  int v16; // [rsp+EA8h] [rbp-5F8h]
  int v17; // [rsp+EACh] [rbp-5F4h]
  int v18; // [rsp+EB0h] [rbp-5F0h]
  int v19; // [rsp+EB4h] [rbp-5ECh]
  int v20; // [rsp+EB8h] [rbp-5E8h]
  char v21[8]; // [rsp+1496h] [rbp-Ah] BYREF

  init();
  printf("uYhESoceNJGkMMFcmjd:");
  input_line(v6, 0x35uLL);
  v6[20] ^= 0xDCu;
  v6[44] ^= 0xC2u;
  v6[9] ^= 0x8Bu;
  v6[52] = ~v6[52];
  v6[26] ^= 0x88u;
  v6[35] ^= 0xC3u;
  v6[43] ^= 0x18u;
  v6[25] ^= 0x91u;
  v6[37] ^= 0xE9u;
  v6[36] ^= 0x99u;
  v6[15] ^= 0xADu;
  v6[40] ^= 0x3Au;
  v6[17] ^= 0x62u;
  v6[49] ^= 0x6Au;
  v6[19] ^= 0x57u;
  v6[39] ^= 0x54u;
  v6[2] ^= 0xFAu;
  v6[27] ^= 0x74u;
  v6[1] ^= 0xFAu;
  v6[45] ^= 0x87u;
  v6[33] ^= 0xA5u;
  v6[30] ^= 0x80u;
  v6[34] ^= 0x6Eu;
  v6[28] ^= 4u;
  v6[0] ^= 0x91u;
  v6[21] ^= 0x91u;
  v6[18] ^= 0xB8u;
  v6[11] ^= 0xA7u;
  v6[5] ^= 0x4Du;
  v6[16] ^= 0xD9u;
  v6[32] ^= 0xEu;
  v6[41] ^= 0xF9u;
  v6[38] ^= 0xF7u;
  v6[13] ^= 0x7Cu;
  v6[22] ^= 0x16u;
  v6[4] ^= 0xA6u;
  v6[6] ^= 0xF5u;
  v6[10] ^= 0x2Fu;
  v6[51] ^= 0x71u;
  v6[24] ^= 0x7Bu;
  v6[8] ^= 0x6Au;
  v6[50] ^= 0x75u;
  v6[12] ^= 0x84u;
  v6[3] ^= 0x77u;
  v6[46] ^= 0xFBu;
  v6[7] ^= 0xB4u;
  v6[47] ^= 0x78u;
  v6[31] ^= 0x8Du;
  v6[29] ^= 0xC7u;
  v6[14] ^= 0xB6u;
  v6[23] ^= 0xACu;
  v6[48] ^= 0xF2u;
  fksth(v6, "erBDJvOroQgOOltKyWMCDpNPlskEHnSundKcbkzcSECamhyzRcNYS");
  printf("lxeaxqgvADxU:");
  input_line(v7, 0x3AuLL);
  v7[26] ^= 0x74u;
  v7[47] ^= 0x61u;
  v7[44] ^= 0x34u;
  v7[36] ^= 0xC2u;
  v7[14] ^= 0x88u;
  v7[7] ^= 0xC4u;
  v7[32] ^= 0x44u;
  v7[39] ^= 0xA7u;
  v7[53] ^= 0x74u;
  v7[33] ^= 0x8Au;
  v7[24] ^= 0xAu;
  v7[20] ^= 0xC3u;
  v7[4] ^= 0x20u;
  v7[0] ^= 0xBFu;
  v7[50] ^= 0x60u;
  v7[22] ^= 0xCDu;
  v7[42] ^= 0xBDu;
  v7[13] ^= 0xC0u;
  v7[34] ^= 0xD6u;
  v7[51] ^= 0xA2u;
  v7[6] ^= 0x23u;
  v7[28] ^= 0x35u;
  v7[16] ^= 0xF1u;
  v7[55] ^= 0xD3u;
  v7[8] ^= 0x3Eu;
  v7[19] ^= 0xD9u;
  v7[31] ^= 0x94u;
  v7[5] ^= 0xF8u;
  v7[35] ^= 0x89u;
  v7[18] ^= 0x7Du;
  v7[29] ^= 0x96u;
  v7[12] ^= 0xCDu;
  v7[30] ^= 0x50u;
  v7[2] ^= 0x52u;
  v7[40] ^= 0xDu;
  v7[49] ^= 0x50u;
  v7[46] ^= 0x24u;
  v7[9] ^= 0x5Cu;
  v7[45] ^= 0x25u;
  v7[10] ^= 0x80u;
  v7[43] ^= 0x76u;
  v7[21] ^= 0xEBu;
  v7[37] ^= 0xD5u;
  v7[15] ^= 2u;
  v7[11] ^= 0xD4u;
  v7[38] ^= 0x39u;
  v7[23] ^= 0x4Eu;
  v7[54] ^= 0xBCu;
  v7[27] ^= 0x1Eu;
  v7[3] ^= 0xBFu;
  v7[25] ^= 0xEAu;
  v7[17] ^= 0x90u;
  v7[52] ^= 0xAu;
  v7[48] ^= 0x65u;
  v7[56] ^= 0xF5u;
  v7[41] ^= 0x51u;
  v7[1] ^= 0x8Du;
  v7[57] ^= 0x81u;
  fksth(v7, "IszDnxOYlZTvaDWGGqlEEOKfwxdzdZTmCmcnXmqQJoAByFzCeHtCmlpVPh");
  printf("uwMGpwrBDSWe:");
  input_line(v4, 0x2DuLL);
  v4[24] ^= 0x27u;
  v4[23] ^= 0x1Fu;
  v4[19] ^= 0x14u;
  v4[18] ^= 0x45u;
  v4[6] ^= 0x27u;
  v4[11] ^= 0x6Du;
  v4[44] ^= 0x3Du;
  v4[0] ^= 0x57u;
  v4[43] ^= 0x99u;
  v4[33] ^= 0x87u;
  v4[7] ^= 0xD8u;
  v4[40] ^= 0x58u;
  v4[1] ^= 0xA9u;
  v4[42] ^= 0x39u;
  v4[12] ^= 0xC8u;
  v4[38] ^= 0xC8u;
  v4[9] ^= 0x6Eu;
  v4[25] ^= 0xA6u;
  v4[35] ^= 0x99u;
  v4[37] ^= 0x40u;
  v4[17] ^= 0x88u;
  v4[30] ^= 0x46u;
  v4[4] ^= 0x8Cu;
  v4[16] ^= 0xF5u;
  v4[13] ^= 0x1Du;
  v4[31] ^= 0x85u;
  v4[28] ^= 0x8Eu;
  v4[34] ^= 0x6Eu;
  v4[26] ^= 0x1Au;
  v4[21] ^= 0xD3u;
  v4[10] ^= 0xA1u;
  v4[39] ^= 0x23u;
  v4[3] ^= 4u;
  v4[20] ^= 0x87u;
  v4[2] ^= 0x42u;
  v4[8] ^= 0x2Du;
  v4[5] ^= 0x6Bu;
  v4[32] ^= 0xF2u;
  v4[27] ^= 0x64u;
  v4[22] ^= 0x51u;
  v4[14] ^= 0x67u;
  v4[15] ^= 0x19u;
  v4[41] ^= 0x38u;
  v4[29] ^= 0x50u;
  fksth(v4, "BxtlTzUyAjCVoNQOTvYpsWjEgKssLGicffdOfdcPLdtem");
  printf("OxIdVxjpxTJNqpXITqJ:");
  input_line(v5, 0x32uLL);
  v5[6] ^= 0xBFu;
  v5[35] ^= 0xA5u;
  v5[4] ^= 0x19u;
  v5[5] ^= 0xBEu;
  v5[3] ^= 0xDAu;
  v5[24] ^= 0x89u;
  v5[33] ^= 0xABu;
  v5[47] ^= 0x10u;
  v5[11] ^= 0x6Au;
  v5[31] ^= 0xEAu;
  v5[45] ^= 0xDDu;
  v5[48] ^= 0x62u;
  v5[14] ^= 0x46u;
  v5[17] ^= 0xB8u;
  v5[8] ^= 0x7Cu;
  v5[12] ^= 0xE6u;
  v5[39] ^= 0xB1u;
  v5[49] ^= 0x2Du;
  v5[43] ^= 0x51u;
  v5[10] ^= 0x43u;
  v5[26] ^= 0xD2u;
  v5[28] ^= 0x5Cu;
  v5[0] ^= 0xAEu;
  v5[2] ^= 0xFDu;
  v5[38] ^= 0x4Eu;
  v5[21] ^= 0x65u;
  v5[16] ^= 0xD0u;Cancel changes
  v5[15] ^= 0xEDu;
  v5[37] ^= 0x9Bu;
  v5[22] ^= 0xA5u;
  v5[20] ^= 0xDu;
  v5[29] ^= 0x46u;
  v5[40] ^= 0x52u;
  v5[19] ^= 0xD0u;
  v5[27] ^= 0xC0u;
  v5[46] ^= 0xE2u;
  v5[9] ^= 0x3Du;
  v5[23] ^= 0x51u;
  v5[44] ^= 0xDEu;
  v5[7] ^= 0x5Cu;
  v5[18] ^= 0xE0u;
  v5[41] ^= 0x51u;
  v5[25] ^= 0xCEu;
  v5[13] ^= 0x42u;
  v5[30] ^= 0xD7u;
  v5[42] ^= 0xEAu;
  v5[32] ^= 0x61u;
  v5[36] ^= 0xDEu;
  fksth(v5, "kfdzDpYjCrDanPfcnQSvDgwHdvkHWOYtpnoFedNGIRDVekFXuc");
  printf("fILdiYbgDG:");
  v14 = input_val();
  v15 = input_val();
  v16 = input_val();
  v17 = input_val();
  v18 = input_val();
  v19 = input_val();
  v20 = input_val();
  result = v15 - v20;
  if ( v15 - v20 == 15303 )
  {
    printf("fLDNbpOcGx:");
    v9 = input_val();
    v10 = input_val();
    v11 = input_val();
    v12 = input_val();
    v13 = input_val();
    printf("ANbzvXWonxh:");
    input_line(v8, 0x3CuLL);
    v8[37] ^= 1u;
    v8[39] ^= 0x49u;
    v8[57] ^= 0x60u;
    v8[45] ^= 0x5Cu;
    v8[43] ^= 0x37u;
    v8[50] ^= 0x7Cu;
    v8[15] ^= 0x30u;
    v8[17] ^= 0x37u;
    v8[33] ^= 0x3Fu;
    v8[21] ^= 0xF0u;
    v8[18] ^= 6u;
    v8[13] ^= 0x15u;
    v8[11] ^= 0xCAu;
    v8[30] ^= 0xCDu;
    v8[58] ^= 0xF0u;
    v8[35] ^= 0x7Du;
    v8[4] ^= 0xA1u;
    v8[8] ^= 0x9Du;
    v8[27] ^= 0x56u;
    v8[41] ^= 0xBCu;
    v8[32] ^= 0xA7u;
    v8[3] ^= 0x75u;
    v8[44] ^= 0x99u;
    v8[23] ^= 0xB8u;
    v8[2] ^= 0xB3u;
    v8[22] ^= 0xE8u;
    v8[5] ^= 0xA0u;
    v8[36] ^= 0xF6u;
    v8[1] ^= 0x59u;
    v8[42] ^= 0xD6u;
    v8[29] ^= 0x6Du;
    v8[59] ^= 0x5Du;
    v8[49] ^= 0xE7u;
    v8[12] ^= 0x9Au;
    v8[56] ^= 0xAEu;
    v8[28] ^= 0x39u;
    v8[54] ^= 0x31u;
    v8[7] ^= 0xBBu;
    v8[51] ^= 0xDFu;
    v8[6] ^= 0x75u;
    v8[46] ^= 0xCEu;
    v8[40] ^= 0xA3u;
    v8[48] ^= 0x8Au;
    v8[25] ^= 0xB4u;
    v8[19] ^= 0x67u;
    v8[9] ^= 0x80u;
    v8[0] ^= 0xD1u;
    v8[52] ^= 0x3Cu;
    v8[55] ^= 0x52u;
    v8[38] ^= 0x6Fu;
    v8[31] ^= 0xCEu;
    v8[16] ^= 0xDEu;
    v8[24] ^= 0xE8u;
    v8[53] ^= 0xEEu;
    v8[14] ^= 0xD7u;
    v8[10] ^= 0x6Du;
    v8[26] ^= 0x2Au;
    v8[34] ^= 0x8Fu;
    v8[20] ^= 0x8Fu;
    result = fksth(v8, "XmbKRdrlwOhqsYGkIFXjKWukNWtnUDRuCVMKInnDDsqnFymarRASiEsCJsdD");
    LOBYTE(result) = result == 0;
    if ( (_BYTE)result )
    {
      printf("tRyPMsjOqo:");
      input_line(v21, 0x32uLL);
      v21[2] ^= 0xCBu;
      v21[7] ^= 0xE6u;
      v21[6] ^= 0xD5u;
      v21[1] ^= 0x21u;
      v21[5] ^= 0x1Au;
      result = fksth(v21, "GybcYZwFN");
      LOBYTE(result) = result == 0;
    }
  }
  return result;
}```
