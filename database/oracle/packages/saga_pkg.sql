-- Packages encapsulate business logic inside DB.

-- Saga orchestrator calls this package to track distributed transactions.

CREATE OR REPLACE PACKAGE SAGA_PKG AS 

    PROCEDURE START_SAGA(
        p_saga_id VARCHAR2,
        p_txn_id VARCHAR2
    );

    PROCEDURE UPDATE_SAGA(
        p_saga_id VARCHAR2,
        p_step VARCHAR2,
        p_status VARCHAR2
    );

END SAGA_PKG;
/


CREATE OR REPLACE PACKAGE BODY SAGA_PKG AS 

PROCEDURE START_SAGA(p_saga_id VARCHAR2, p_txn_id VARCHAR2) IS
BEGIN
    INSERT INTO SAGA_STATE
    VALUES (p_saga_id, p_txn_id, "START", "IN_PROGRESS", SYSTIMESTAMP);
END;

PROCEDURE UPDATE_SAGA(p_saga_id VARCHAR2, p_step VARCHAR2, p_status VARCHAR2) IS
BEGIN
    UPDATE INTO SAGA_STATE
    SET CURRENT_STEP = p_step,
        STATUS = p_status,
        UPDATED_AT = SYSTIMESTAMP
    WHERE SAGA_ID = p_saga_id;
END;

END SAGA_PKG;
/
