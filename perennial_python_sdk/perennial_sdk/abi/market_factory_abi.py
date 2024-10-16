market_factory_abi = [
    {
        "inputs": [
            {
                "internalType": "contract IFactory",
                "name": "oracleFactory_",
                "type": "address",
            },
            {
                "internalType": "address",
                "name": "implementation_",
                "type": "address",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "FactoryAlreadyRegisteredError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "FactoryInvalidOracleError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "FactoryInvalidPayoffError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "FactoryNotInstanceError",
        "type": "error",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "version",
                "type": "uint256",
            },
        ],
        "name": "InitializableAlreadyInitializedError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "InitializableNotInitializingError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "InitializableZeroVersionError",
        "type": "error",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
        ],
        "name": "OwnableNotOwnerError",
        "type": "error",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
        ],
        "name": "OwnableNotPendingOwnerError",
        "type": "error",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
        ],
        "name": "PausableNotPauserError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "PausablePausedError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "ProtocolParameterStorageInvalidError",
        "type": "error",
    },
    {
        "inputs": [],
        "name": "ProtocolParameterStorageInvalidError",
        "type": "error",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "version",
                "type": "uint256",
            },
        ],
        "name": "Initialized",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "contract IInstance",
                "name": "instance",
                "type": "address",
            },
        ],
        "name": "InstanceRegistered",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "contract IMarket",
                "name": "market",
                "type": "address",
            },
            {
                "components": [
                    {
                        "internalType": "Token18",
                        "name": "token",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IOracleProvider",
                        "name": "oracle",
                        "type": "address",
                    },
                ],
                "indexed": False,
                "internalType": "struct IMarket.MarketDefinition",
                "name": "definition",
                "type": "tuple",
            },
        ],
        "name": "MarketCreated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "newEnabled",
                "type": "bool",
            },
        ],
        "name": "OperatorUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnerUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "UFixed6",
                        "name": "protocolFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFeeAbsolute",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxCut",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxRate",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minMaintenance",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minEfficiency",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "referralFee",
                        "type": "uint256",
                    },
                ],
                "indexed": False,
                "internalType": "struct ProtocolParameter",
                "name": "newParameter",
                "type": "tuple",
            },
        ],
        "name": "ParameterUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "Paused",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newPauser",
                "type": "address",
            },
        ],
        "name": "PauserUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newPendingOwner",
                "type": "address",
            },
        ],
        "name": "PendingOwnerUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "referrer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "UFixed6",
                "name": "newFee",
                "type": "uint256",
            },
        ],
        "name": "ReferralFeeUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "Unpaused",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "acceptOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "Token18",
                        "name": "token",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IOracleProvider",
                        "name": "oracle",
                        "type": "address",
                    },
                ],
                "internalType": "struct IMarket.MarketDefinition",
                "name": "definition",
                "type": "tuple",
            },
        ],
        "name": "create",
        "outputs": [
            {
                "internalType": "contract IMarket",
                "name": "newMarket",
                "type": "address",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "implementation",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IInstance",
                "name": "instance",
                "type": "address",
            },
        ],
        "name": "instances",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IOracleProvider",
                "name": "oracle",
                "type": "address",
            },
        ],
        "name": "markets",
        "outputs": [
            {
                "internalType": "contract IMarket",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "name": "operators",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "oracleFactory",
        "outputs": [
            {
                "internalType": "contract IFactory",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "parameter",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "UFixed6",
                        "name": "protocolFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFeeAbsolute",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxCut",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxRate",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minMaintenance",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minEfficiency",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "referralFee",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct ProtocolParameter",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pauser",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pendingOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "name": "referralFee",
        "outputs": [
            {
                "internalType": "UFixed6",
                "name": "",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "internalType": "bool",
                "name": "newEnabled",
                "type": "bool",
            },
        ],
        "name": "updateOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "UFixed6",
                        "name": "protocolFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFee",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxFeeAbsolute",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxCut",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "maxRate",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minMaintenance",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "minEfficiency",
                        "type": "uint256",
                    },
                    {
                        "internalType": "UFixed6",
                        "name": "referralFee",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct ProtocolParameter",
                "name": "newParameter",
                "type": "tuple",
            },
        ],
        "name": "updateParameter",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPauser",
                "type": "address",
            },
        ],
        "name": "updatePauser",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newPendingOwner",
                "type": "address",
            },
        ],
        "name": "updatePendingOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "referrer",
                "type": "address",
            },
            {
                "internalType": "UFixed6",
                "name": "newReferralFee",
                "type": "uint256",
            },
        ],
        "name": "updateReferralFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]