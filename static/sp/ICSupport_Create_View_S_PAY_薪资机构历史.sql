CREATE VIEW [dbo].[S_PAY_薪资架构历史] AS
select (SELECT TOP 1 PERSONID FROM  PSNACCOUNT WHERE ACCESSIONSTATE = 2)PERSONID
,org.UNITCODE,org.UNITNAME,psn.EMPLOYEEID,psn.TRUENAME
,SubLog.subjectid,Sub.subjectname 科目名称,SubLog.subjectsum 金额,Kind.CURRENCYNAME 币种
,SubLog.effecttime 生效日期,SubLog.disabledtime 失效日期 
,SubLog.lastedituserid 最后修改人,SubLog.lastedittime 最后修改时间,PC.ITEMNAME 修改原因
	FROM PAYPERSONALCALCULATESUBJECTLOG SubLog,PAYPAYROLLSUBJECT Sub ,PAYCURRENCYKIND Kind,PAYPAYROLLPUBCODEITEM Pc 
		,PSNACCOUNT Psn,ORGSTDSTRUCT Org  
		where 1=1 AND pc.ITEMID=SubLog.CHANGEREASON AND Pc.CODEID = '003' 
			and Sub.payrollsubjectid=SubLog.subjectid  and Kind.CURRENCYID=SubLog.currencykind 
			and SubLog.USERID=psn.PERSONID and psn.BRANCHID = org.UNITID
			and org.ISTEMPUNIT = 0    
GO