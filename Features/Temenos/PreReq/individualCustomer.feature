@container=PreReq
Feature: Verify that STO is created with blocked account

  Scenario Outline: Verify that user is able to create individual normal customer
    Given user is on Temenos Home Screen
    When user enters "<HelpTaextMenu>" in "Navbar_Commandline"
    And user clicks on "Navbar_ExecuteCommandline"
    And user waits for new window to appear
    And user clicks on "Show/Hide Menu"
    And user clicks on "Customer"
    And user clicks on "Customer Normal Creation"
    And user clicks on "Individual Customer"
    And user selects "<Title>" from "Customer_TitleDropdown"
    And user enters "<FirstName>" in "Customer_FirstName1"
    And user enters "<LastName>" in "Customer_LastName"
    And user enters "<ShortName>" in "Customer_ShortName"
    And user enters "<MotherMaidenName>" in "Customer_MotherMaidenName"
    And user enters "<FatherHusbandName>" in "Customer_FatherHusbandName"
    And user clicks on "<Gender>" in "Customer_Gender" radio button
    And user selects "<MaritalStatus>" from "Customer_MaritalStatus"
    And user enters "<AccountOfficer>" in "Customer_AccountOfficer"
    And user clicks on "Customer_BranchNameDropdownButton"
    And user clicks on "<BranchName>" from dropdown
    And wait
    And user clicks on "Customer_SectorDropdownButton"
    And user clicks on "<Sector>" from dropdown
    And user enters "<Industry>" in "Customer_Industry"
    And wait
    And user enters "<Target>" in "Customer_Target"
    And user enters "<Status>" in "Customer_Status"
    And user enters "<Nationality>" in "Customer_Nationality"
    And user clicks on "<Religion>" in "Customer_Religion" radio button
    And user clicks on "<ZakatOption>" in "Customer_Zakat" radio button
    And wait
    And user enters "<Segment>" in "Customer_Segment"
    And wait
    And user enters "<PlaceOfBirth>" in "Customer_PlaceOfBirth"
    And user enters "<Residence>" in "Customer_Residence"
    And user enters "<Customer_DateOfBirth>" in "Customer_DateOfBirth"
    And user enters "<Language>" in "Customer_Language"
    And user clicks on "Customer_IDDoc"
    And user enters "<LegalID>" in "Customer_IDDoc_LegalID"
    And user clicks on "Customer_IDDoc_IDType1DropdownButton"
    And user clicks on "<IDType>" from dropdown
    And user enters "<IssueDate>" in "Customer_IDDoc_IssueDate"
    And user enters "<ExpiryDate>" in "Customer_IDDoc_ExpiryDate"
    And user clicks on "Mailing Address" tab
    And user enters "<Address>" in "Customer_MailingAddress_Address1"
    And user enters "<City>" in "Customer_MailingAddress_City"
    And user enters "<MobileNumber>" in "Customer_MailingAddress_MobileNumber"
    And user clicks on "Customer_EmploymentBusiness"
    And user enters "<Occupation>" in "Customer_EmploymentBusiness_Occupation"
    And user clicks on "KYC" tab
    And user selects "<FundSRCOccasional>" from "Customer_KYC_FundSRCOccasional"
    And user enters "<MntlyCRTurnoverAmt>" in "Customer_KYC_MntlyCRTurnoverAmt"
    And user enters "<MntlyCRTurnoverNoOFTxn>" in "Customer_KYC_MntlyDRTurnoverAmt"
    And user enters "<MntlyDRTurnoverAmt>" in "Customer_KYC_MntlyCRTurnoverTxn"
    And user enters "<MntlyDRTurnoverNoOFTxn>" in "Customer_KYC_MntlyDRTurnoverTxn"
    And user enters "<PEP>" in "Customer_KYC_PEP"
    And user clicks on "Action_Validate"
    And user clicks on "Action_Commit"
    And wait
    Then completion message should appear in "Action_VerificationMessage"

    Examples:
      | HelpTextMenu | Title | FirstName | LastName | ShortName | MotherMaidenName | FatherHusbandName | Gender | MaritalStatus | AccountOfficer | BranchName | Sector | Industry | Target | Status | Nationality | Religion | ZakatOption | Residence | Segment | PlaceOfBirth | Residence | Customer_DateOfBirth | Language | LegalID | IDType | IssueDate   | ExpiryDate  | Address                                   | City    | MobileNumber | Occupation | FundSRCOccasional       | MntlyCRTurnoverAmt | MntlyCRTurnoverNoOFTxn | MntlyDRTurnoverAmt | MntlyDRTurnoverNoOFTxn | PEP |
      | ?251         | MR    | Nabeel    | Arif     | SNAA      | Mother           | Arif Hussain      | MALE   | Unmarried     | 1              | PK0020015  | 1000   | 1000     | 1      | 1      | PK          | Muslim   | No          | PK        | 1       | PK           | PK        | 15 MAR 1990          | 1        | CNIC    | CNIC   | 16 Aug 2021 | 10 Aug 2030 | House No. 5, Capital Housing society, Khi | Karachi | 03342121011  | 1          | Contribution By Members | 1                  | 1                      | 1                  | 1                      | 0   |

  @authorization  @NO
  Scenario Outline: [Pre-Req]Primary Customer Authorization for Joint Account Opening with Zakat Exempt as No [EN-1714]
    Given user is on Temenos Home Screen
    When user enters "<HelpTextMenu>" in "Navbar_Commandline"
    And user clicks on "Navbar_ExecuteCommandline"
    And user waits for new window to appear
    And user clicks on "Home_Menu"
    And user clicks on "Home_Customer"
    And user clicks on "Home_CustomerNormalCreation"
    And user clicks on "Home_CustomerNormalAuthoriseDelete"
    And user clicks on "Authorize_ToggleMenu"
    And user clicks on "Authorize_Filter"
    And user enters "<Code>" in "Authorize_CustomerCode"
    And user clicks on "Authorize_FindButton"
    And user clicks on "Authorize_AuthorizeExpand"
    And user clicks on "Authorize_AuthorizeButton"
    And wait
    Then completion message should appear in "Action_VerificationMessageAuthorize"

    Examples:
      | HelpTextMenu | Code |
      | ?251         | Code |