class Const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__: # 判断是否已经被赋值，如果是则报错
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper(): # 判断所赋值是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)
        self.__dict__[name] = value


const = Const()
const.ABI = '[{"constant":false,"inputs":[],"name":"register","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"vote_upload_complete","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vote_statistics_complete","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"concatInterceptAndCoef","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"vote_statistics","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"back_manager","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"clear_after_one_epoch","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"user_num","type":"uint256"}],"name":"mstart","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"valid_intercept","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"curr_beneficiary","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_intercept","type":"string"},{"internalType":"string","name":"_coef","type":"string"}],"name":"upload_param","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"download_param","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"all_user_registered","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAllCoef","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"start","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"user_address","type":"address"},{"internalType":"uint256","name":"sequence","type":"uint256"}],"name":"pay","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"param_upload_complete","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAllIntercept","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"valid_coef","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"end","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"votes","type":"string"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"}]'
const.BYTECODE = "608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506120b7806100606000396000f3fe60806040526004361061012a5760003560e01c806399d9b9d8116100ab578063c40768761161006f578063c407687614610560578063d3d7b854146105ae578063dec9a9bf146105d9578063e58160cb14610669578063efbe1c1c146106f9578063fc36e15b146107245761012a565b806399d9b9d8146102f0578063a6eea5251461044f578063ae5210931461047a578063ba779ed6146104a5578063be9a6555146105355761012a565b80637426ae54116100f25780637426ae54146101ba578063794d8e77146101c457806386546e6b146101ce57806386c0276814610209578063972608da146102995761012a565b80631aa3a0081461012c5780631d4633e31461014357806324a678dd1461016e5780636d049eb1146101995780636fcbdb62146101b0575b005b34801561013857600080fd5b506101416107ec565b005b34801561014f57600080fd5b5061015861082a565b6040518082815260200191505060405180910390f35b34801561017a57600080fd5b50610183610830565b6040518082815260200191505060405180910390f35b3480156101a557600080fd5b506101ae610836565b005b6101b8610d96565b005b6101c26111e5565b005b6101cc611266565b005b3480156101da57600080fd5b50610207600480360360208110156101f157600080fd5b81019080803590602001909291905050506113b2565b005b34801561021557600080fd5b5061021e61153a565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561025e578082015181840152602081019050610243565b50505050905090810190601f16801561028b5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156102a557600080fd5b506102ae6115d8565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156102fc57600080fd5b5061044d6004803603604081101561031357600080fd5b810190808035906020019064010000000081111561033057600080fd5b82018360208201111561034257600080fd5b8035906020019184600183028401116401000000008311171561036457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001906401000000008111156103c757600080fd5b8201836020820111156103d957600080fd5b803590602001918460018302840111640100000000831117156103fb57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506115fe565b005b34801561045b57600080fd5b506104646116bc565b6040518082815260200191505060405180910390f35b34801561048657600080fd5b5061048f6116c2565b6040518082815260200191505060405180910390f35b3480156104b157600080fd5b506104ba6116c8565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156104fa5780820151818401526020810190506104df565b50505050905090810190601f1680156105275780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561054157600080fd5b5061054a61176a565b6040518082815260200191505060405180910390f35b6105ac6004803603604081101561057657600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050611770565b005b3480156105ba57600080fd5b506105c36117bf565b6040518082815260200191505060405180910390f35b3480156105e557600080fd5b506105ee6117c5565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561062e578082015181840152602081019050610613565b50505050905090810190601f16801561065b5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561067557600080fd5b5061067e611867565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156106be5780820151818401526020810190506106a3565b50505050905090810190601f1680156106eb5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561070557600080fd5b5061070e611905565b6040518082815260200191505060405180910390f35b34801561073057600080fd5b506107ea6004803603602081101561074757600080fd5b810190808035906020019064010000000081111561076457600080fd5b82018360208201111561077657600080fd5b8035906020019184600183028401116401000000008311171561079857600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050919291929050505061190b565b005b600a546001600b540111610807576001600b5401600b819055505b600a54600b541415610828576000600b819055506001600f5401600f819055505b565b60105481565b60115481565b60606040518060200160405280600081525090506060604051806020016040528060008152509050600680549050600580549050146108c0576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602b815260200180612058602b913960400191505060405180910390fd5b6000600580549050141561093c576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601a8152602001807f63757272656e7420696e7465726365707473206973206e756c6c00000000000081525060200191505060405180910390fd5b600060068054905014156109b8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260158152602001807f63757272656e7420636f656673206973206e756c6c000000000000000000000081525060200191505060405180910390fd5b60008090505b600160058054905003811015610bd357610a8783600583815481106109df57fe5b906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610a7d5780601f10610a5257610100808354040283529160200191610a7d565b820191906000526020600020905b815481529060010190602001808311610a6057829003601f168201915b50505050506119ef565b9250610ac8836040518060400160405280600181526020017f3b000000000000000000000000000000000000000000000000000000000000008152506119ef565b9250610b838260068381548110610adb57fe5b906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610b795780601f10610b4e57610100808354040283529160200191610b79565b820191906000526020600020905b815481529060010190602001808311610b5c57829003601f168201915b50505050506119ef565b9150610bc4826040518060400160405280600181526020017f3b000000000000000000000000000000000000000000000000000000000000008152506119ef565b915080806001019150506109be565b600580549050811015610d5757610c998360058381548110610bf157fe5b906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610c8f5780601f10610c6457610100808354040283529160200191610c8f565b820191906000526020600020905b815481529060010190602001808311610c7257829003601f168201915b50505050506119ef565b9250610d548260068381548110610cac57fe5b906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610d4a5780601f10610d1f57610100808354040283529160200191610d4a565b820191906000526020600020905b815481529060010190602001808311610d2d57829003601f168201915b50505050506119ef565b91505b8260079080519060200190610d6d929190611e5b565b508160089080519060200190610d84929190611e5b565b506001600e5401600e81905550505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610e58576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601e8152602001807f4f6e6c79206f776e65722063616e20636f756e742074686520766f746573000081525060200191505060405180910390fd5b6060600a54604051908082528060200260200182016040528015610e8b5781602001602082028038833980820191505090505b509050610e96611edb565b600080600090505b600a5481101561103f57610f6060098281548110610eb857fe5b906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610f565780601f10610f2b57610100808354040283529160200191610f56565b820191906000526020600020905b815481529060010190602001808311610f3957829003601f168201915b5050505050611a14565b9250600091505b6001600a540382101561100157610fd6610fcf610fca610fbb6040518060400160405280600181526020017f2c00000000000000000000000000000000000000000000000000000000000000815250611a14565b86611a4290919063ffffffff16565b611a5c565b6000611abe565b848381518110610fe257fe5b6020026020010181815101915081815250508180600101925050610f67565b61101461100d84611a5c565b6000611abe565b84838151811061102057fe5b6020026020010181815101915081815250508080600101915050610e9e565b506000809050600080905060008090505b600a5481101561109c5785818151811061106657fe5b602002602001015182101561108f5785818151811061108157fe5b602002602001015191508092505b8080600101915050611050565b50600682815481106110aa57fe5b90600052602060002001600290805460018160011615610100020316600290046110d5929190611ef5565b50600582815481106110e357fe5b906000526020600020016003908054600181600116156101000203166002900461110e929190611ef5565b506004828154811061111c57fe5b9060005260206000200160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506111ca6004838154811061119757fe5b9060005260206000200160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600a54611770565b6111d2611266565b6001601154016011819055505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050158015611263573d6000803e3d6000fd5b50565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614611328576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601e8152602001807f4f6e6c79206f776e65722063616e20636c65617220746865207374617465000081525060200191505060405180910390fd5b6001600a5403600a819055506000600b819055506008600061134a9190611f7c565b600760006113589190611f7c565b600660006113669190611fc4565b600560006113749190611fc4565b600460006113829190611fe5565b600960006113909190611fc4565b6000600a5414156113b0576113a36111e5565b6001601254016012819055505b565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614611474576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601d8152602001807f4f6e6c79206f776e65722063616e2073746172742074686520766f746500000081525060200191505060405180910390fd5b80600a819055506000600b819055506000600c819055506000600d819055506000600e819055506000600f81905550600060108190555060006011819055506000601281905550600260006114c99190611f7c565b600360006114d79190611f7c565b600860006114e59190611f7c565b600760006114f39190611f7c565b600660006115019190611fc4565b6005600061150f9190611fc4565b6004600061151d9190611fe5565b6009600061152b9190611fc4565b6001600c5401600c8190555050565b60038054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156115d05780601f106115a5576101008083540402835291602001916115d0565b820191906000526020600020905b8154815290600101906020018083116115b357829003601f168201915b505050505081565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600a546001600b540111611697576001600b5401600b819055506005829080600181540180825580915050906001820390600052602060002001600090919290919091509080519060200190611655929190611e5b565b50506006819080600181540180825580915050906001820390600052602060002001600090919290919091509080519060200190611694929190611e5b565b50505b600a54600b5414156116b8576000600b819055506001600d5401600d819055505b5050565b600e5481565b600f5481565b606060088054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156117605780601f1061173557610100808354040283529160200191611760565b820191906000526020600020905b81548152906001019060200180831161174357829003601f168201915b5050505050905090565b600c5481565b8173ffffffffffffffffffffffffffffffffffffffff166108fc6103e883029081150290604051600060405180830381858888f193505050501580156117ba573d6000803e3d6000fd5b505050565b600d5481565b606060078054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561185d5780601f106118325761010080835404028352916020019161185d565b820191906000526020600020905b81548152906001019060200180831161184057829003601f168201915b5050505050905090565b60028054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156118fd5780601f106118d2576101008083540402835291602001916118fd565b820191906000526020600020905b8154815290600101906020018083116118e057829003601f168201915b505050505081565b60125481565b600a546001600b5401116119cb576001600b5401600b819055506009819080600181540180825580915050906001820390600052602060002001600090919290919091509080519060200190611962929190611e5b565b505060043390806001815401808255809150509060018203906000526020600020016000909192909190916101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505b600a54600b5414156119ec576000600b819055506001601054016010819055505b50565b60608083905060608390506060611a068383611bd1565b905080935050505092915050565b611a1c611edb565b600060208301905060405180604001604052808451815260200182815250915050919050565b611a4a611edb565b611a55838383611c99565b5092915050565b60608082600001516040519080825280601f01601f191660200182016040528015611a965781602001600182028038833980820191505090505b5090506000602082019050611ab48185602001518660000151611d37565b8192505050919050565b600060608390506000809050600080905060008090505b8351811015611bb2576030848281518110611aec57fe5b602001015160f81c60f81b60f81c60ff1610158015611b2857506039848281518110611b1457fe5b602001015160f81c60f81b60f81c60ff1611155b15611b7a578115611b4b576000861415611b4157611bb2565b8580600190039650505b600a830292506030848281518110611b5f57fe5b602001015160f81c60f81b60f81c60ff160383019250611ba5565b602e848281518110611b8857fe5b602001015160f81c60f81b60f81c60ff161415611ba457600191505b5b8080600101915050611ad5565b506000851115611bc55784600a0a820291505b81935050505092915050565b606082826040516020018083805190602001908083835b60208310611c0b5780518252602082019150602081019050602083039250611be8565b6001836020036101000a03801982511681845116808217855250505050505090500182805190602001908083835b60208310611c5c5780518252602082019150602081019050602083039250611c39565b6001836020036101000a03801982511681845116808217855250505050505090500192505050604051602081830303815290604052905092915050565b611ca1611edb565b6000611cbf8560000151866020015186600001518760200151611d80565b90508460200151836020018181525050846020015181038360000181815250508460000151856020015101811415611d01576000856000018181525050611d2c565b8360000151836000015101856000018181510391508181525050836000015181018560200181815250505b829150509392505050565b5b60208110611d5b5781518352602083019250602082019150602081039050611d38565b60006001826020036101000a0390508019835116818551168181178652505050505050565b6000808490506000868511611e4b5760208511611e0557600060018660200360080260020a031960001b905060008186511690506000878a8a0103905060008386511690505b828114611df757818610611de4578a8a019650505050505050611e53565b8580600101965050838651169050611dc6565b859650505050505050611e53565b60008585209050600091505b8588038211611e49576000868420905080821415611e355783945050505050611e53565b600184019350508180600101925050611e11565b505b868601925050505b949350505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10611e9c57805160ff1916838001178555611eca565b82800160010185558215611eca579182015b82811115611ec9578251825591602001919060010190611eae565b5b509050611ed79190612006565b5090565b604051806040016040528060008152602001600081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10611f2e5780548555611f6b565b82800160010185558215611f6b57600052602060002091601f016020900482015b82811115611f6a578254825591600101919060010190611f4f565b5b509050611f789190612006565b5090565b50805460018160011615610100020316600290046000825580601f10611fa25750611fc1565b601f016020900490600052602060002090810190611fc09190612006565b5b50565b5080546000825590600052602060002090810190611fe2919061202b565b50565b50805460008255906000526020600020908101906120039190612006565b50565b61202891905b8082111561202457600081600090555060010161200c565b5090565b90565b61205491905b8082111561205057600081816120479190611f7c565b50600101612031565b5090565b9056fe496e76616c69642063757272656e7420696e7465726365707473206f722063757272656e7420636f656673a265627a7a723158203438fa4ffb5a0391754da4369c637cf6c1ab6ad2a59ac01c15edfc01d1b665c564736f6c634300050b0032"
const.GANACHE_URL = "wss://ropsten.infura.io/ws/v3/747b0843f2e04ab7a384fa175deba232"
# const.CONTRACT_ADDRESS = "0x489B2D45069a26f50efb5a99A90B5EAd2541981c" 第一次在infura上部署的Ballot4

# 本地ganache上的测试合约
# const.GANACHE_URL = "http://127.0.0.1:7545"
# const.CONTRACT_ADDRESS = "0x7796Ed61cC20B5052cE4dd3cAcFdc14157CCD12e"

#第二次在infura上部署的Ballot4
# const.CONTRACT_ADDRESS = "0xE31807108DCa90cE0FFD21e7fbf15a064D1C0776"
#第三次在infura上部署的Ballot4 'gasUsed': 1829230
# const.CONTRACT_ADDRESS = "0x6628aBcAAb55CF4DCc4e82A5EF3D769A7DD95891"
# 第一次在infura上部署的Ballot5 'gasUsed': 1789864，在Ballot4的基础上加上了价值转移
# const.CONTRACT_ADDRESS = "0x457fC29958E2696B379809B7FEFFA64987Cff24B"
# 第二次在infura上部署的Ballot5 'gasUsed': 1789864，将event改为利用uint表示状态, 该智能合约存在一个问题，调用mstart时，transaction receipt中的status总是0，即该方程执行不成功
# 但是调用其他的方程可以成功，暂且不清楚原因。另外，发现solidity中的require在web3.py使用buildTransaction()创建rawTransaction时就会发挥作用，但程序会提示的是超出gas限制。
# const.CONTRACT_ADDRESS = "0xF28f3B7b1708900cb28Ada92134D1aB757E1B9C8"
# 第二次在infura上部署的Ballot5 未改动智能合约
const.CONTRACT_ADDRESS = "0x700401683403e3041032FB0B93D877974Fd7362D"

