create PROCEDURE usp_AlterExtendView
	(@VIEWNAME NVARCHAR(100),@GROUPNAME NVARCHAR(200))
as
-- exec usp_AlterExtendViem @GROUPNAME = '异地发薪记录',@VIEWNAME = 'S_PAY_MultiSalaryCal'
	begin
	DECLARE @GROUPID NVARCHAR(40),@GROUPTYPE NVARCHAR(2),@DATETABLENAME NVARCHAR(100),@DETAILTABLENAME NVARCHAR(100), @SQL NVARCHAR(4000),@TMPSQL NVARCHAR(4000)
	DECLARE @SQL1 NVARCHAR(4000),@SQL2 NVARCHAR(4000),@SQL3 NVARCHAR(4000),@STRi NVARCHAR(10),@ITEMID NVARCHAR(40),@ITEMNAME NVARCHAR(200),@i int; 

	SELECT @GROUPID = GROUPID,@GROUPTYPE = GROUPTYPE From Payextenddatagroup where isdeleted=0 and GROUPNAME=@GROUPNAME
	IF @GROUPTYPE = '1'
		begin
		SET @DATETABLENAME = 'PAYORGBUSINESSDATA';
		SET @DETAILTABLENAME = 'PAYORGBUSINESSDATADETAIL';
		end
	else if @GROUPTYPE = '0'
		begin
		SET @DATETABLENAME = 'PAYPERSONBUSINESSDATA';
		SET @DETAILTABLENAME = 'PAYPERSONBUSINESSDATADETAIL';
		end
		
	SET @SQL = 'alter view dbo.'+@VIEWNAME+' AS
	With extendMain as (Select * From '+@DATETABLENAME+' Where Groupid ='''+@GROUPID+''')
	,extendDetail AS (
		select * from '+@DETAILTABLENAME+' 
			where itemid in (Select ITEMID From Payextenddatagroupitem Where Groupid ='''+@GROUPID+''')
	)
	select ';


	SET @TMPSQL = 'declare My_Cursor cursor for Select ITEMID,ITEMNAME From Payextenddatagroupitem Where ISDELETED = 0 and Groupid ='''+@GROUPID+''' order by ITEMORDER';
	exec(@TMPSQL);
	SET @SQL1 = '1 Fal';SET @SQL2 = 'from extendMain ';
	SET @SQL3 = '';SET @STRi = '';SET @i = 0;
	OPEN My_Cursor; 
	FETCH NEXT FROM My_Cursor into @ITEMID,@ITEMNAME ; 
	WHILE @@FETCH_STATUS = 0
	BEGIN
	SET @i =@i +1
	SELECT @STRi = 'detail'+CONVERT(NVARCHAR(10),@i);
	SET @SQL1 =@SQL1+','+@STRi+'.ITEMVALUE '+@ITEMNAME
	SET @SQL3 =@SQL3+' left join extendDetail '+@STRi+' on extendMain.DATAID='+@STRi+'.DATAID and '+@STRi+'.ITEMID ='''+@ITEMID+'''';
	FETCH NEXT FROM My_Cursor into @ITEMID,@ITEMNAME ; 
	END
	CLOSE My_Cursor; 
	DEALLOCATE My_Cursor;
	PRINT @SQL;PRINT @SQL1;PRINT @SQL2;PRINT @SQL3;
	exec (@SQL + @SQL1 + @SQL2 + @SQL3);
end