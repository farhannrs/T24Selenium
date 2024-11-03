@Hajj_Application_Form_Authorization
Feature: Hajj- Authorize hajj Application form

  Scenario Outline: [pre-Req]Hajj- creating normal request
    Given user is on Temenos Home Screen
    When user enters "<HelpTextMenu>" in "Navbar_Commandline"
    And user clicks on "Navbar_ExecuteCommandline"
    And user waits for new window to appear
    And user clicks on "Home_Menu"
    And user clicks on "Hajj_HajjBranchOperations"
    And user clicks on "Hajj_HajjApplication"
    And user clicks on "Hajj_HajjApplicationForm"
    And user enters "<HajjInput>" in "Hajj_HajjInput"
    And user clicks on "ContractScreen_EditButton"
    And user enters "<CNIC>" in "Hajj_CNIC"
    And user enters "<MoraId>" in "Hajj_MoraId"
    And user enters "<ApplicantName>" in "Hajj_SurName"
    And user enters "<ApplicantName>" in "Hajj_ApplicantName"
    And user clicks on "Customer_Gender"
    And user enters "<MobileNumber>" in "Hajj_MobileNumber"
    And user enters "<FatherName>" in "Hajj_FatherName_HusbandName"
    And user enters "<Address>" in "Hajj_Address"
    And user selects "<POD>" from "Hajj_POD"
    And user enters "<DOB>" in "Hajj_DOB"
    And user clicks on "Hajj_AgeGroupAdult"
    And user clicks on "Action_Validate"
    And user clicks on "Action_Commit"
    Then completion message should appear in "Action_VerificationMessage"

    Examples:
      | HelpTextMenu | HajjInput | CNIC | MoraId | ApplicantName | FatherName | Address      | MobileNumber | RefundAccountNumber | POD     | AgeGroup       | DOB         |
      | ?268         | hajjID    | CNIC | hajjID | farhan        | test       | test address | 03458081145  | Account No          | KARACHI | Senior Citizen | 16 Aug 2021 |

  @authorization
  Scenario Outline: Hajj- Authorize hajj Application form
    Given user is on Temenos Home Screen
    When user enters "<HelpTextMenu>" in "Navbar_Commandline"
    And user clicks on "Navbar_ExecuteCommandline"
    And user waits for new window to appear
    And user clicks on "Home_Menu"
    And user clicks on "Hajj_BranchOperations"
    And user clicks on "Hajj_Applications"
    And user clicks on "Hajj_AuthorizeApplicationForm"
    And user enters "<Code>" in "IPOCentralized_AppID"
    And user clicks on "Authorize_FindButton"
    And user clicks on "IPOCentralized_Select"
    And user clicks on "Hajj_AuthCheck"
    And user clicks on "<value>" alert
    Then record should be updated successfully

    Examples:
      | HelpTextMenu | Code | value  |
      | ?268         | Code | accept |