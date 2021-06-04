pragma solidity 0.5.11;

import "./strings.sol";
//import "github.com/oraclize/ethereum-api/provableAPI_0.5.sol";
//import "https://github.com/provable-things/ethereum-api/blob/master/oraclizeAPI_0.5.sol";

contract Ballot5{
    using strings for *;

    address payable owner;

    address public curr_beneficiary;
    
    string public valid_coef;
    string public valid_intercept;

    address payable[] curr_addresses;
    string[] curr_intercepts;
    string[] curr_coefs;

    string all_intercepts;
    string all_coefs;

    string[] curr_votes;

    uint valid_user_num;
    uint curr_user_num;
    
    uint public start;
    uint public param_upload_complete;
    uint public download_param;
    uint public all_user_registered;
    uint public vote_upload_complete;
    uint public vote_statistics_complete;
    uint public end;
    
    constructor() public {
        owner = msg.sender;
    }
    //manager
    function mstart(uint user_num) public {
        require(
            msg.sender == owner,
            "Only owner can start the vote"
        );
        valid_user_num = user_num;
        curr_user_num = 0;

        start = 0;
        param_upload_complete = 0;
        download_param = 0;
        all_user_registered = 0;
        vote_upload_complete = 0;
        vote_statistics_complete = 0;
        end = 0;
        
        delete valid_coef;
        delete valid_intercept;
        delete all_coefs;
        delete all_intercepts;

        delete curr_coefs;
        delete curr_intercepts;
        delete curr_addresses;
        delete curr_votes;
        delete curr_beneficiary;

        start = start + 1;
    }

    //manager
    function clear_after_one_epoch() public payable {

        require(
            msg.sender == owner,
            "Only owner can clear the state"
        );

        valid_user_num = valid_user_num - 1;
        curr_user_num = 0;
        
        delete all_coefs;
        delete all_intercepts;

        delete curr_coefs;
        delete curr_intercepts;
        delete curr_addresses;
        delete curr_votes;

        if(valid_user_num == 0)
        {
            back_manager();
            end = end + 1;
        }
    }

    //manager
    function vote_statistics() public payable {

        require(
            msg.sender == owner,
            "Only owner can count the votes"
        );

        uint[] memory vote_result = new uint[](valid_user_num);
        strings.slice memory vote_slice;
        uint j;
        for(uint i = 0; i < valid_user_num; i++)
        {
            vote_slice = curr_votes[i].toSlice();
            j = 0;
            for(; j < valid_user_num - 1; j++)
            {
                vote_result[j] += parseInt(vote_slice.split(",".toSlice()).toString(), 0);
            }
            vote_result[j] += parseInt(vote_slice.toString(), 0);
        }

        uint max_vote_index = 0;
        uint max_vote = 0;
        for(uint i = 0; i < valid_user_num; i++)
        {
            if(max_vote < vote_result[i])
            {
                max_vote = vote_result[i];
                max_vote_index = i;
            }
        }

        valid_coef = curr_coefs[max_vote_index];
        valid_intercept = curr_intercepts[max_vote_index];
        
        curr_beneficiary = curr_addresses[max_vote_index];
        
        pay(curr_addresses[max_vote_index], valid_user_num);
        clear_after_one_epoch();
        vote_statistics_complete = vote_statistics_complete + 1;
        
    }

    //contract
    //reward user for sharing information
    function pay(address payable user_address, uint sequence) public payable {
        user_address.transfer(sequence * 1000);
    }

    //contract
    //return the rest ether to manager
    function back_manager() public payable {
        owner.transfer(address(this).balance);
    }

    //user
    function register() public {
        if (curr_user_num + 1 <= valid_user_num)
        {
            curr_user_num = curr_user_num + 1;
        }
        if(curr_user_num == valid_user_num)
        {
            curr_user_num = 0;
            all_user_registered = all_user_registered + 1;
        }
    }

    //user
    function upload_param(string memory _intercept, string memory _coef) public {
        if (curr_user_num + 1 <= valid_user_num)
        {
            curr_user_num = curr_user_num + 1;
            curr_intercepts.push(_intercept);
            curr_coefs.push(_coef);
        }
        if(curr_user_num == valid_user_num)
        {
            curr_user_num = 0;
            param_upload_complete = param_upload_complete + 1;
        }
    }

    //user
    function vote(string memory votes) public {
        if(curr_user_num + 1 <= valid_user_num)
        {
            curr_user_num = curr_user_num + 1;
            curr_votes.push(votes);
            curr_addresses.push(msg.sender);
        }
        if(curr_user_num == valid_user_num)
        {
            curr_user_num = 0;
            vote_upload_complete = vote_upload_complete + 1;
        }
    }

    //manager concatenate all intercepts to a single string
    function concatInterceptAndCoef() public {
        string memory tmp_intercepts = "";
        string memory tmp_coefs = "";
        require(
            curr_intercepts.length == curr_coefs.length,
            "Invalid current intercepts or current coefs"
        );
        require(
            curr_intercepts.length != 0,
            "current intercepts is null"
        );
        require(
            curr_coefs.length != 0,
            "current coefs is null"
        );
        uint i = 0;
        for(; i < curr_intercepts.length - 1; i++)
        {
            tmp_intercepts = strConcat(tmp_intercepts, curr_intercepts[i]);
            tmp_intercepts = strConcat(tmp_intercepts, ";");
            tmp_coefs = strConcat(tmp_coefs, curr_coefs[i]);
            tmp_coefs = strConcat(tmp_coefs, ";");
        }
        if(i < curr_intercepts.length)
        {
            tmp_intercepts = strConcat(tmp_intercepts, curr_intercepts[i]);
            tmp_coefs = strConcat(tmp_coefs, curr_coefs[i]);
        }
        all_intercepts = tmp_intercepts;
        all_coefs = tmp_coefs;

        download_param = download_param + 1;
    }

    //user
    function getAllIntercept() public view returns (string memory) {
        return all_intercepts;
    }

    //user
    function getAllCoef() public view returns (string memory) {
        return all_coefs;
    }

    //tools
    function parseInt(string memory _a, uint _b) internal pure returns (uint _parsedInt) {
        bytes memory bresult = bytes(_a);
        uint mint = 0;
        bool decimals = false;
        for (uint i = 0; i < bresult.length; i++) {
            if ((uint(uint8(bresult[i])) >= 48) && (uint(uint8(bresult[i])) <= 57)) {
                if (decimals) {
                   if (_b == 0) {
                       break;
                   } else {
                       _b--;
                   }
                }
                mint *= 10;
                mint += uint(uint8(bresult[i])) - 48;
            } else if (uint(uint8(bresult[i])) == 46) {
                decimals = true;
            }
        }
        if (_b > 0) {
            mint *= 10 ** _b;
        }
        return mint;
    }

    //tools : concatenate bytes
    function bytesConcat(bytes memory a, bytes memory b)
            internal pure returns (bytes memory) {
        return abi.encodePacked(a, b);
    }
    //tools : concatenate strings
    function strConcat(string memory _a, string memory  _b) internal pure returns (string memory){
        bytes memory _ba = bytes(_a);
        bytes memory _bb = bytes(_b);
        bytes memory result = bytesConcat(_ba, _bb);
        return string(result);
    }

    // Fallback function for sending ether to this contract
    function () external payable {}

}
