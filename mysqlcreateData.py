#!/usr/bin/env python# -*- coding: utf-8 -*-import mysqlInPutDataTool as mysqltoolimport xlrd# CREATE TABLE `sanguogame`.`new_table` (#   `id` INT NOT NULL AUTO_INCREMENT,#   `name` VARCHAR(45) NOT NULL,#   `class` VARCHAR(45) NOT NULL,#   `age` VARCHAR(45) NOT NULL,#   PRIMARY KEY (`id`));#数据表路径#策划数据表basescheme = 'gametable/basescheme.xlsx'#游戏服务器数据配制表netscheme = 'gametable/netscheme.xlsx'#服务器数据配制表serverscheme = 'gametable/serverscheme.xlsx'#说明，基础表与游戏服务器数据表是放在游戏数据库中,所有数据与游戏逻辑相关。服务器数据表是放在服务器数据库中,所有数据与玩家帐号及服务器相关#mysql连接工具mysqlt = mysqltool.mysqlTool()#读取excel数据表到listdef getTables(excelf):    tables = {}    xlrd.Book.encoding = "cp1252"    wb = xlrd.open_workbook(excelf)    for sheetName in wb.sheet_names():        if len(sheetName) > 10 and sheetName[:10]=="servertab_":#服务器配置表            sheet = wb.sheet_by_name(sheetName)            for i in range(0,sheet.ncols):                            if sheet.cell(2,i).value=='':                    nclows=i                    break                else:                    nclows=sheet.ncols                           print nclows,sheet.nrows            tablelines = []            for rownum in range(0,sheet.nrows):                tmplines = []                if rownum == 2:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value).upper())                elif rownum > 3:                    for nnumber in range(0,nclows):                        if len(tablelines[2][nnumber]) >= 3 and tablelines[2][nnumber][:3] == 'INT':                            if sheet.cell(rownum,nnumber).ctype == 2:#ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error                                tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        elif len(tablelines[2][nnumber]) >= 5 and tablelines[2][nnumber][:5] == 'FLOAT':                            tmplines.append(str(sheet.cell(rownum,nnumber).value))                        elif len(tablelines[2][nnumber]) >= 7 and tablelines[2][nnumber][:7] == 'VARCHAR' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                                                                    elif len(tablelines[2][nnumber]) >= 4 and tablelines[2][nnumber][:4] == 'TEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        elif len(tablelines[2][nnumber]) >= 10 and tablelines[2][nnumber][:10] == 'MEDIUMTEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        else:                            tmplines.append(str(sheet.cell(rownum,nnumber).value))                else:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value))                tablelines.append(tmplines)            tmpt = {'database':'server','table':tablelines}            tables[sheetName] = tmpt        elif len(sheetName) > 7 and sheetName[:7]=="nettab_":#服务器配置表            sheet = wb.sheet_by_name(sheetName)            for i in range(0,sheet.ncols):                            if sheet.cell(2,i).value=='':                    nclows=i                    break                else:                    nclows=sheet.ncols                           print nclows,sheet.nrows            tablelines = []            for rownum in range(0,sheet.nrows):                tmplines = []                if rownum == 2:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value).upper())                elif rownum > 3:                    for nnumber in range(0,nclows):                        if len(tablelines[2][nnumber]) >= 3 and tablelines[2][nnumber][:3] == 'INT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(sheet.cell(rownum,nnumber).value)                        elif len(tablelines[2][nnumber]) >= 5 and tablelines[2][nnumber][:5] == 'FLOAT':                            tmplines.append(sheet.cell(rownum,nnumber).value)                        elif len(tablelines[2][nnumber]) >= 7 and tablelines[2][nnumber][:7] == 'VARCHAR' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        elif len(tablelines[2][nnumber]) >= 4 and tablelines[2][nnumber][:4] == 'TEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        elif len(tablelines[2][nnumber]) >= 10 and tablelines[2][nnumber][:10] == 'MEDIUMTEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value)))                        else:                            tmplines.append(str(sheet.cell(rownum,nnumber).value))                else:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value))                tablelines.append(tmplines)            tmpt = {'database':'net','table':tablelines}            tables[sheetName] = tmpt        elif len(sheetName) > 4 and sheetName[:4]=="tab_":#服务器配置表            sheet = wb.sheet_by_name(sheetName)            for i in range(0,sheet.ncols):                            if sheet.cell(2,i).value=='':                    nclows=i                    break                else:                    nclows=sheet.ncols                           print nclows,sheet.nrows            tablelines = []            for rownum in range(0,sheet.nrows):                tmplines = []                if rownum == 2:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value).upper())                elif rownum > 3:                    for nnumber in range(0,nclows):                        print sheet.cell(rownum,nnumber).value(),sheet.cell(rownum,nnumber).ctype                        if len(tablelines[2][nnumber]) >= 3 and tablelines[2][nnumber][:3] == 'INT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(sheet.cell(rownum,nnumber).value())                        elif len(tablelines[2][nnumber]) >= 5 and tablelines[2][nnumber][:5] == 'FLOAT':                            tmplines.append(sheet.cell(rownum,nnumber).value())                        elif len(tablelines[2][nnumber]) >= 7 and tablelines[2][nnumber][:7] == 'VARCHAR' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value())))                        elif len(tablelines[2][nnumber]) >= 4 and tablelines[2][nnumber][:4] == 'TEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value())))                        elif len(tablelines[2][nnumber]) >= 10 and tablelines[2][nnumber][:10] == 'MEDIUMTEXT' and sheet.cell(rownum,nnumber).ctype == 2:                            tmplines.append(str(int(sheet.cell(rownum,nnumber).value())))                        else:                            tmplines.append(sheet.cell(rownum,nnumber).value())                else:                    for nnumber in range(0,nclows):                        tmplines.append(str(sheet.cell(rownum,nnumber).value))                tablelines.append(tmplines)            tmpt = {'database':'base','table':tablelines}            tables[sheetName] = tmpt    return tables#读取所有基础表表头def getAllBaseTableHand():    tablesmap = getTables(basescheme)    return tablesmap#读取所有游戏网络数据配置表表头def getAllNetTableHand():    tablesmap = getTables(netscheme)    return tablesmap#读取所有登陆服务器配置表表头def getAllserverTableHand():    tablesmap = getTables(serverscheme)    return tablesmap    # INSERT INTO `game`.`nettab_account` (`account_k`, `name_uq`, `accounttype`, `gem`, `gole`, `ancientbook`, `forage`, `herosoul`, `militaryexploit`, `medal`, `exp`, `level`, `vip`, `tongID`, `tongnumber`) VALUES ('aaaa', '111', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');# INSERT INTO `game`.`nettab_account` (`account_k`, `name_uq`, `accounttype`, `gem`, `gole`, `ancientbook`, `forage`, `herosoul`, `militaryexploit`, `medal`, `exp`, `level`, `vip`, `tongID`, `tongnumber`) VALUES ('bbb', '22', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');#创建server用户数据库，并创建数据表def createServerDataBaseStr(tabsmap):    #SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME='server'; #判断server数据库是否存在    #CREATE SCHEMA IF NOT EXISTS `server`;  #创建数据库    print 'mysql',mysqlt    #sqlcmd = "SELECT * FROM information_schema.SCHEMATA"    #CREATE SCHEMA `new_schema` DEFAULT CHARACTER SET utf8 ;    sqlcmd = "CREATE SCHEMA IF NOT EXISTS `server` DEFAULT CHARACTER SET utf8;\n"    tabcmd = ''        for tn in tabsmap.keys():        tname = tn        tdat = tabsmap[tname]['table']        ttype = tabsmap[tname]['database']        print tabsmap[tname]['table']        print ttype        tmpstr = ''        insetcmd = ''        insetLinescmd = ''        if ttype == 'server':            tmpstr += "CREATE TABLE `%s`.`%s` (\n"%('server',tname)            insetcmd = "INSERT INTO `%s`.`%s` ("%('server',tname)            for n in range(len(tdat[0])):                c = tdat[0][n]                tmpstr += "`%s` %s NOT NULL"%(c,tdat[2][n])                if 'key' in str(tdat[3][n]).split(','):                    tmpstr += " "                if c[:2] == 'id' and tdat[2][n][:3] == 'INT':                    tmpstr += " AUTO_INCREMENT,\n"                else:                    tmpstr += ",\n"                #数据库插入数据表                insetcmd += "`%s`,"%(tdat[0][n])            insetcmd = insetcmd[:-1] + ") VALUES ("            tmpstr += "PRIMARY KEY ("            for yi in range(len(tdat[0])):                c = tdat[0][yi]                if 'key' in str(tdat[3][yi]).split(','):                    tmpstr += "`%s`,"%(c)            tmpstr = tmpstr[:-1] + "),\n"            for yi2 in range(len(tdat[0])):                c = tdat[0][yi2]                if 'uq' in str(tdat[3][yi2]).split(','):                    tmpstr += "UNIQUE INDEX `%s_UNIQUE` (`%s` ASC),\n"%(c,c)            tmpstr = tmpstr[:-2] + ")DEFAULT CHARSET=utf8;\n"            for l in range(len(tdat)):                if l < 4:                    continue                linetmp = tdat[l]                insetLinescmd += insetcmd                for dcell in range(len(linetmp)):                    if len(tdat[2][dcell]) >= 3 and tdat[2][dcell][:3] == 'INT':                        insetLinescmd += "'%d',"%(int(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 5 and tdat[2][dcell][:5] == 'FLOAT':                        insetLinescmd += "'%f',"%(float(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 7 and tdat[2][dcell][:7] == 'VARCHAR':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 4 and tdat[2][dcell][:4] == 'TEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 10 and tdat[2][dcell][:10] == 'MEDIUMTEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                insetLinescmd = insetLinescmd[:-1] + ");\n"        tabcmd += tmpstr        tabcmd += insetLinescmd    sqlcmd += tabcmd    return sqlcmd            #在server数据库中插入数据行def insetDataToServerDataBase(tablename,datlines):    pass#删除服务器数据库数据行def deleteDataFromServerDataBase(tablename,datlines):    pass#修改server数据库中的数据行def updateToServerDataBase(tablename,datlines):    pass#查找server数据库数据def searchDataFromServerDataBase(tablename,idkey,cond = ''):#cond:查询条件    pass#创建game数据库,并创建基础数据表和游戏角色数据表def createGameDataBaseStr(tabnetmap,tabbasemap = {}):    print 'mysql',mysqlt    #sqlcmd = "SELECT * FROM information_schema.SCHEMATA"    # CREATE SCHEMA IF NOT EXISTS `server` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;    sqlcmd = "CREATE SCHEMA IF NOT EXISTS `game` DEFAULT CHARACTER SET utf8;\n"    tabcmd = ''    for tn in tabnetmap.keys():        tname = tn        tdat = tabnetmap[tname]['table']        ttype = tabnetmap[tname]['database']#         print tabnetmap[tname]['table']#         print ttype        tmpstr = ''        insetcmd = ''#数据表中插入数据命令        insetLinescmd = ''  #数据表中插入数据命令        if ttype == 'net':            tmpstr += "CREATE TABLE `%s`.`%s` (\n"%('game',tname)            insetcmd = "INSERT INTO `%s`.`%s` ("%('game',tname)            for n in range(len(tdat[0])):                c = tdat[0][n]                tmpstr += "`%s` %s NOT NULL"%(c,tdat[2][n])                if 'key' in str(tdat[3][n]).split(',') and tdat[2][n][:3] == 'INT':                    tmpstr += " AUTO_INCREMENT,\n"                else:                    tmpstr += ",\n"                #数据库插入数据表                insetcmd += "`%s`,"%(tdat[0][n])#数据表中插入数据命令            insetcmd = insetcmd[:-1] + ") VALUES ("#数据表中插入数据命令            tmpstr += "PRIMARY KEY ("            for y1 in range(len(tdat[0])):                #print c                c = tdat[0][y1]                if 'key' in str(tdat[3][y1]).split(','):                    tmpstr += "`%s`,"%(c)            tmpstr = tmpstr[:-1] + "),\n"            for y2 in range(len(tdat[0])):                c = tdat[0][y2]                if 'uq' in str(tdat[3][y2]).split(','):                    tmpstr += "UNIQUE INDEX `%s_UNIQUE` (`%s` ASC),\n"%(c,c)            tmpstr = tmpstr[:-2] + ")DEFAULT CHARSET=utf8;\n"            #数据表中插入数据命令            for l in range(len(tdat)):                if l < 4:                    continue                linetmp = tdat[l]                insetLinescmd += insetcmd                for dcell in range(len(linetmp)):                    if len(tdat[2][dcell]) >= 3 and tdat[2][dcell][:3] == 'INT':                        insetLinescmd += "'%d',"%(int(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 5 and tdat[2][dcell][:5] == 'FLOAT':                        insetLinescmd += "'%f',"%(float(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 7 and tdat[2][dcell][:7] == 'VARCHAR':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 4 and tdat[2][dcell][:4] == 'TEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 10 and tdat[2][dcell][:10] == 'MEDIUMTEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                insetLinescmd = insetLinescmd[:-1] + ");\n"        tabcmd += tmpstr        tabcmd += insetLinescmd#数据表中插入数据命令    sqlcmd += tabcmd    tabcmd = ''    for tn in tabbasemap.keys():        tname = tn        tdat = tabbasemap[tname]['table']        ttype = tabbasemap[tname]['database']#         print tabbasemap[tname]['table']#         print ttype        tmpstr = ''        insetcmd = ''#数据表中插入数据命令        insetLinescmd = ''  #数据表中插入数据命令        if ttype == 'base':            tmpstr += "CREATE TABLE `%s`.`%s` (\n"%('game',tname)            insetcmd = "INSERT INTO `%s`.`%s` ("%('game',tname)            for n in range(len(tdat[0])):                c = tdat[0][n]                tmpstr += "`%s` %s NOT NULL,\n"%(c,tdat[2][n])                #数据库插入数据表                insetcmd += "`%s`,"%(tdat[0][n])#数据表中插入数据命令            insetcmd = insetcmd[:-1] + ") VALUES ("#数据表中插入数据命令            tmpstr += "PRIMARY KEY ("            for y0 in range(len(tdat[0])):                c = tdat[0][y0]                if 'key' in str(tdat[3][y0]).split(','):                    tmpstr += "`%s`,"%(c)            tmpstr = tmpstr[:-1] + "),\n"            for y1 in range(len(tdat[0])):                c = tdat[0][y1]                if 'uq' in str(tdat[3][y1]).split(','):                    tmpstr += "UNIQUE INDEX `%s_UNIQUE` (`%s` ASC),\n"%(c,c)            tmpstr = tmpstr[:-2] + ")DEFAULT CHARSET=utf8;\n"            #数据表中插入数据命令            for l in range(len(tdat)):                if l < 4:                    continue                linetmp = tdat[l]                insetLinescmd += insetcmd                for dcell in range(len(linetmp)):                    if len(tdat[2][dcell]) >= 3 and tdat[2][dcell][:3] == 'INT':                        insetLinescmd += "'%d',"%(int(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 5 and tdat[2][dcell][:5] == 'FLOAT':                        insetLinescmd += "'%f',"%(float(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 7 and tdat[2][dcell][:7] == 'VARCHAR':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 4 and tdat[2][dcell][:4] == 'TEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                    elif len(tdat[2][dcell]) >= 10 and tdat[2][dcell][:10] == 'MEDIUMTEXT':                        insetLinescmd += "'%s',"%(str(linetmp[dcell]))                insetLinescmd = insetLinescmd[:-1] + ");\n"        tabcmd += tmpstr        tabcmd += insetLinescmd#数据表中插入数据命令    sqlcmd += tabcmd    return sqlcmd    #在game数据库中插入数据行def insetDataToGameDataBase(tablename,datlines):    pass#删除game服务器数据库数据行def deleteDataFromGameDataBase(tablename,datlines):    pass#修改game数据库中的数据行def updateToGameDataBase(tablename,datlines):    pass#查找game数据库数据def searchDataFromGameDataBase(tablename,idkey,cond = ''):#cond:查询条件    pass#主方法def main():    tmap = getAllserverTableHand()    cmdsql = createServerDataBaseStr(tmap)    netp = getAllNetTableHand()    cmdsql += createGameDataBaseStr(netp)    print 'cmd:\n'    #print cmdsql    f = open('inputdat.txt','w')    f.write(cmdsql)    f.close()    #sqlpath = filedirtool.cur_file_dir() + '/inputdat.sql'    #mysqlt.inPutDataWithSqlFile(sqlpath)    backsql = mysqlt.execute(cmdsql.encode('utf-8'))    print 'game mysql:',backsqlif __name__ == '__main__':    main()