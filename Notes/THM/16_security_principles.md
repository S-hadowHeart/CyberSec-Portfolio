# CIA
- _Confidentiality , Integrity , Availability_
- Before we can decribe something as secure , we need to consider better what makes up security.
- when you want to judege the security of system , you need to think in terms of security triad:
- Confidentialiy , integrity, and availbility (CIA)
  - __Confidentiality__ ensures that only the intended persons or recipients can access the data.
  - __Integrity__ aims to ensure that the data cannot be altered; moreover, we can detect any alteration if it occurs.
  - __Availability__ aims to ensure that the system or service is available when needed.
- __Confidentiality :__
  - during online shopping , you expect your credit card number to be disclosed only to the entity that processes the payment.
  - if you doubt that your credit card information will be disclosed to an untrusted party,you will most likely refrain from continuing with transcation.
  - Moreover , if a data breach results in the disclosure of personally identifiable information, including credit cards, the company will incur huge losses on multiple levels.
 
  - According to various laws in modern countries, healthcare providers must ensure and maintain the confidentiality of medical records.
  - Consequently , healthcare providers can be held legally accountable if they illegally disclose their patients' medical records
- __Integrity :__
  - after filing out your order , if an intruder can alter the shipping address you have submitted ,
  - the package will be sent to someone else.
  - wihtout data integrity , you might be very reluctant to place your order with this seller.
 
  - if patient record is accidentally or maliciously altered, it can lead to the wrong treatment being administered,
  - which, in turn, can lead to a life-threatening situation.
  - Hence, the system would be useless and potentially harmful without ensuring the integrity of medical records.
- __Availablity :__
  - To place your online order , you will either browse the store's website or use its official app.
  - if the service is unavailable , you  won't be able to browse the products or place an order if you continue to face such technical issues,
  - you might eventually give up and start looking for different online store.
 
  - when patient visits a clinic to follow up on their medical  condition , the system must be available.
  - An unvaliable system would mean that the medical practitioner cannot access the patient's records
  - And consequently won't know if any current symptoms are related to the patient's medical history.
  - This situation can make the medical diagnosis more challenging and error-prone.
 
- __Authenticity :__
  - Authentic means not fraudulent or counterfeit.
  - Authenticity is about ensuring that the document/file/data is from the claimed source.
- __Nonerepudiation :__
  - Repudiate means refusing to recognize the validity of something.
  - Nonrepudiation ensures that original source cannot deny that they are the source of a particular document/file/data.
  - This characteristic is indispensable for various domains, such as shopping , patient diagnosis and banking.
These two requirements are closely related. The need to tell authentic files or order s from fake ones is indispensable.
Moreover, ensuring that the other party cannot deny being the source is vital for many systems to be usable.

- __Utility :__
  - Utility focuses on the uefulness of the information.
  - For instance, a use might have lost the decryption key to access a laptop with encrypted storage.
  - Although the user still has the laptop with its disk(s) intact, they cannot access them.
  - in other words , although still available the information is in form that is not useful, i.e., of no utility
 
- __Possession :__
  - THis security element requires that we protect the information from unauthorized taking , copying or controlling.
  - For instance , an adversary might take backup drive , meaning we loss possession of the information as long as they have the drive.
  - Alternatively, the adversary might succeed in encrypting our data using randomware; this also leads to the loss of possession of the data.


## DAD [Disclosure , Alteration , Destruction/Denial]
- The security of system is attacked through one of several means.
- it can be via the disclosure of secret data, alteration of data , or destruction of data.

- __Disclosure :__
  - is the opposite of confidentiality.
  - disclosure of confidential data would be an attack on confidentiality.
- __Alteration :__
  - is the opposite of integrity.
  - Example : the integrity of a cheque is indispensable
 
- __Destruction/Denial:__
  - is the opposite of Availability

## Fundamental Concepts of Security Models
- __Bell-LaPadula Model :__
  - __Simple security Property:__
    - This Property is referred to as "no read up";
    - it states that a subject at a lower security level cannot read an object at higher security level.
    - This rule Prevents access to sensitive information above the authrized level.
  - __Star security Property :__
    - This property is referred to as "no write down";
    - it states that a subject at a higher securtiy level cannot write to an object at lower security level.
    - This rule prevents the discloure of sensitive information to a subject of lower seucrity level.
  - __Discretionary-Security Property :__
    - This property uses an access matrix to allow read and write operations.
    - An example access matrix is shown in the table below and used in conjunction with the first two properties.

  - The first two propertities can be summarized as "write up , read down".
  - you can share confidential information with people of high securtiy clarance (write up),
  - and you can receive confidential information from people with lower with lower securtiy clearance (read down).
  - There are certain limitations to the Bell-LaPadula model.
  - Example : it was not designed to handle file-sharing.
 
  ## Biba Model
  - The Biba Model aims to achieve __inegrity__ by specifitying two main rules:
    - __simple integrity Property :__
      - This property is referred to as "no read down";
      - A higher integrity subject should not read from a lower integrity object.
    - __Star integrity Property :__
      - This property is referred to as "no write up";
      - A lower integrity subject should not write to a higher integrity object.
  - These two properties can be summarized as "read up, write down."
  - This rule is in contrast with the Bell-LaPadula Model,
  - And this should not be surprising as one is concerned with confidentiality while the other is with integrity
  - Biba Model suffers from various limitations.
  - One example is that it does not handle internal threats (insider threat).
 
  ## Clark-Wilson Model
  - The Clark-wilson Model also aims to achieve integrity by using the following concepts:
  - __Constrained Data iteam(CDI) :
    - This refers to the data type whose integrity we want to preserve.
  - __Unconstrained Data item (UDI) :
    - These procedures are programmed operations, such as read and write, and should maintain the integrity of CDIs.
  - __Transformation Procedures (TPs) :__
    - These procedures are programmed operations , such as read and write and should maintain the integrity of CDIs
  - __Integrity verification Procedures (IVPs) :__
    - These procedures check and ensure the validity of CDIs

  ## Defence-in-Depth
  - refers to creating a securtiy system of multiple levels
  - hence it is also called __Multi-Level security__.

  ## ISO/IEC 19249
  - The international Organization for Standardization (ISO) and International Electotechnical Commission  (IEC) have created the ISO/IEC 19249.
  - The purpose is to have a better idea of what international organizations would teach regarding security  principles.
  1. __Domain Separation :__
     - Every set related components is grouped as a single entity;
     - components can be applications,data, or other resources.
     - Each entity will have its own domain and be assigned a common set of security attributes.
     - Example, consider the x86 processor privilege levels:the operating system kernel can run in ring 3 (the lease privileged level).
     - Domain separation is included in the Goguen-Meseguer Model.
  2. __Layering :__
     - when a system is structured  into may abstract levels or layers,
     - it becomes possible to impose security policies at different levels;
     - moreover, it would be feasible to validate the operation.
     - Let's consider the OSI (Open Systems interconnection) model with  its seen layers in networking.
     - Each layer in the OSI model provides specific services to the layer above it.
     - This layering makes it possible to impose security policies and easily validate that the system is working as intended.
     - Another example from the programming language hides the low-level system calls and presents them as more user-friendly methods . Layering relates defence in Depth.
       
  3. __Encapsulation :__
     - in oop, we hide low-level implementations and prevent direct manipulation of the data in an object by providing specific methods for that purpose.
     - Example , if you have a clock object, you would provide a method  `increment()` instead of giving the user direct access to the `seconds` variable.
     - The aim is prevent invalid values for your variables.
     - Similarly , in larger systems, you would use (or even design) a proper application programming interface (API) that your application would use to access the database.
  4. __Redundancy :__
    - The principle ensures availabiltiy and integrity.
    - There are examples related to redundacy.
    - Consider the case of a hardware server with two built-in power supplies:
      - if one power supply fails , the system continues to function.
      - Consider a RAID 5 configuration with three drives:
        - if one drive fails, data remains avaliable using the remaining two drives.
        - Moreover , if data is improperly changed on one of the disks,
        - it would be detected via the parity , ensuring the data's integrity.
  5. __virtualization :__
    - with the advent of cloud services, virualization has become more common and popular.
    - The concept of virtualization is sharing a single set of hardware among muliple operating systems.
    - virtualization provides sandboxing capabilities that imporve security boundaries, secure detonation, and observance of malicious porgrams.
  ## 5 Design principles:
  1. __Least Privilege :__
    - you can also phrase it infomally as "need-to basis" or "need-to-know basis" as you answer the  question , "Who can access  what?"
    - The principle of least privailege teches that you should provide the least amount of permissions for someone to carry out their task and nothing more.
    - For example , if a user needs to be able to view a document , you should give them read rights without wirte rights.
  2. __Attack Surface Minimisation :__
    - Every system has vulnerabilities that and attacker might use to compromise a system.
    - Some vulnerabilities are known , while others are yet to be discovered.
    - These vulnerabilities represent risks that we should aim to minimize.
    - For example, in one of the steps to harden a Linux system , we would disable any service we don't need.
  3. __Centralized Parameter Validation :__
    - Many threats are due to the system receiving input,especially from users.
    - invalid inputs can be used to exploit vulnerabilities in the system, such as denial of service and remote code execution.
    - Therefore,parameter validation is a necessary step to ensure the correct system state.
    - Considering the number of parameters a system handles,
    - the validation of the parameters should be centralized within one library or system.
  4. __Centralized General Security Services :__
    - As a security principle , we should aim to centralize all security services.
    - For example, we would create a centralized server for authentication.
    - Of course , you might take proper measures to ensure availability and prevent creating a single point of failure.
  5. __Preparing for Error and Exception Handling :__
    - whever we build a system, we should take into account that errors and exceptions do and will occur.
    - For instance, in a shopping application, a customer might try to place an order for an out-of-stock item.
    - A database might get overloaded and stop responding to a web application.
    - This principle teaches that the systems should be designed to fail safe; for example, if a firewall crashes, it should block all traffic instead of allowing all traffic.
    - Moreover , we should be careful that error messages don't leak information that we confidential, such as dumping memory content that contains infomation related to other customers.
 
- Trust is a very complex topic; in reality, we cannot without  function without trust.
- if one were to think that the laptop vendor has installed spyware on the laptop, they would most likely end up rebuilding the system.
- if one were to mistrust the hardware vendor , they would stop using it completely.
- if we think of trust on business level, things only become more sophisticaated;
- however, we need some guiding security principles.
- Two security principles that are of interest to use regarding trust:
  - Trust but verify
  - Zero Trust
- __Trust but Verify :__
  - This principle teaches that we should always verify even when we trust an entity and its behaviour.
  - An entity might be a user or a system.
  - verifying usually requires setting up proper logging mechanisms;
  - verifying indicates going through the logs to ensure everything is normal.
  - in reality, it is not feasible to verify everything; just think of the work it takes to review all the actions taken by a single entity, such as internet pages browsed by single user.
  - This requires automated seucrity mechanisms, such as proxy , intrusion detection , and intrusion prevention systems.

- __Zero Trust :__
  - This principle treats trust as a vulnerability, and consequently , it caters to insider-related threats.
  - After considering trust as vulnerability, zero trust tries to eliminate it.
  - it is teaching indirectly, "never trust,always verify."
  - in other words , every entity is considered adversarial until proven otherwise.
  - Zero trust does not grant trust to a device based on its location or ownership.
  - This approach contrasts with older models that would trust internal networks or enterprise-owned devices.
  - Authentication and authorization are required before accessing any resource.
  - As a result , if any breach occurs, the damage would be more contained if a zero architecture had been implemented.
 
- Microsegmentation is one of the implementations used for Zero Trust.
- it refers to the design where a network segment can be as small as sigle host.
- Moreover, communication between segments requires authentication, access control list checks , and otehr security requirements.

- There is a limti to how much we apply zero trust without negatively impacting a business;
- however, this does not mean that we should not apply it long as it is feasible.

- There are three terms that we need to take nore of to avoid any confusion.
- __Vulnerability :__
  - Vulnerable means susceptible to attack or damage.
  - in information security, a vulnerability is a weakness.
- __Threat :__
  - A threat is potential danger associated with this weakness or vulnerability.
- __Risk :__
  - The risk is concerned  with like likelihood of a threat actor exploiting a vulnerabiltiy and the consequent impact on the business.
 
- Away from information systems , a showroom with doors and windows made of standard glass suffers a weakness , or vulnerability, due to the nature of glass.
- Consequently, there is a threat that the glass doors and windows can be broken.
- The showroom owners should contemplate the risk, i.e. the likelihood that a glass door or window gets broken and the resulting impact on the business.

- Consider another example directly related to information systems.
- you work for a hospital that uses a  particular databse system to store all the medical records.
- One day, you are following the latest seucriy news, and you learn that the used databse sytem is not only vulnerable but also a proof-of-concept working exploit code has beedn relased;
- the released exploit code indicates that the threat is real.
- with this knowledge, you must consider the resulting risk and ecide the next steps.
