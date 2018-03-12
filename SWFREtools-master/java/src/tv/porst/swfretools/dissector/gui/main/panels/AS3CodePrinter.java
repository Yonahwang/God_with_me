package tv.porst.swfretools.dissector.gui.main.panels;

import java.util.List;

import tv.porst.swfretools.parser.actions.as3.*;
import tv.porst.swfretools.parser.structures.AS3Code;
import tv.porst.swfretools.parser.structures.MethodInfo;
import tv.porst.swfretools.utils.ActionScript3Helpers;
import tv.porst.swfretools.utils.as3.ResolvedClass;
import tv.porst.swfretools.utils.as3.ResolvedCode;
import tv.porst.swfretools.utils.as3.ResolvedMethod;

/**
 * Contains functions that turn ActionScript 3 code into a string that can
 * be displayed to the user.
 */
public final class AS3CodePrinter {

	/**
	 * Adds a simple one-mnemonic instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The instruction mnemonic.
	 */
	private static void add(final StringBuilder sb, final String mnemonic) {
		sb.append(mnemonic);
	}

	/**
	 * Adds an instruction with one argument to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The instruction mnemonic.
	 * @param value The instruction argument value.
	 */
	private static void add(final StringBuilder sb, final String mnemonic, final long value) {
		sb.append(String.format("%s %d", mnemonic, value));
	}

	/**
	 * Adds an instruction with two arguments to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The instruction mnemonic.
	 * @param value1 The first instruction argument value.
	 * @param value2 The second instruction argument value.
	 */
	private static void add(final StringBuilder sb, final String mnemonic, final long value1, final long value2) {
		sb.append(String.format("%s %d, %d", mnemonic, value1, value2));
	}

	/**
	 * Adds the class footer to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 */
	private static void addClassFooter(final StringBuilder sb) {
		sb.append("}\n\n");
	}

	/**
	 * Adds the class header to the output.
	 * 
	 * @param resolvedClass Provides the class information.
	 * @param sb The string builder the output is appended to.
	 */
	private static void addClassHeader(final ResolvedClass resolvedClass, final StringBuilder sb) {
		sb.append("class ");

		// Add the class name.
		final String className = ActionScript3Helpers.flattenNamespaceName(resolvedClass.getName());
		sb.append(className);

		// Add the opening class parentheses.
		sb.append("\n{\n");
	}

	/**
	 * Resolves and adds a double value to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param doubleIndex The double index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addDouble(final StringBuilder sb, final String mnemonic, final int doubleIndex, final ResolvedCode code) {

		final Double dbl = code.resolveDouble(doubleIndex - 1);

		sb.append(mnemonic);
		sb.append(" ");

		if (dbl == null) {
			sb.append(String.format("??? [0x%08X]", doubleIndex));
		}
		else {
			sb.append(String.format("%f [0x%08X]", dbl, doubleIndex));
		}
	}

	/**
	 * Adds an if instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the if instruction.
	 * @param value The branch offset value.
	 */
	private static void addIf(final StringBuilder sb, final String mnemonic, final long value) {
		sb.append(String.format("%s %08X", mnemonic, value));
	}

	/**
	 * Adds an instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param instruction The instruction to add to the output.
	 * @param code The code the instruction belongs to.
	 * @param firstOffset The offset of the first instruction in the code.
	 */
	private static void addInstructionText(final StringBuilder sb, final AS3Instruction instruction, final ResolvedCode code, final int firstOffset) {

		new AS3Visitor() {

			@Override
			protected void visit(final AS3Add instruction) {
				add(sb, "add");
			}

			@Override
			protected void visit(final AS3Addi instruction) {
				add(sb, "addi");
			}

			@Override
			protected void visit(final AS3Astype instruction) {
				addMultiname(sb, "add", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Astypelate instruction) {
				add(sb, "typelate");
			}

			@Override
			protected void visit(final AS3Bitand instruction) {
				add(sb, "bitand");
			}

			@Override
			protected void visit(final AS3Bitnot instruction) {
				add(sb, "bitnot");
			}

			@Override
			protected void visit(final AS3Bitor instruction) {
				add(sb, "bitor");
			}

			@Override
			protected void visit(final AS3Bitxor instruction) {
				add(sb, "bitxor");
			}

			@Override
			protected void visit(final AS3Call instruction) {
				add(sb, "call", instruction.getArgCount().value());
			}

			@Override
			protected void visit(final AS3Callmethod instruction) {
				final String methodName = getMethodName(instruction.getIndex().value(), code);

				if (methodName == null) {
					sb.append(String.format("callmethod ???, %d", instruction.getArgCount().value()));
				} else {
					sb.append(String.format("callmethod %s, %d", instruction.getArgCount().value()));
				}
			}

			@Override
			protected void visit(final AS3Callproperty instruction) {
				addMultinameInteger(sb, "callproperty", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Callproplex instruction) {
				addMultinameInteger(sb, "callproplex", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Callpropvoid instruction) {
				addMultinameInteger(sb, "callpropvoid", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Callstatic instruction) {
				final String methodName = getMethodName(instruction.getIndex().value(), code);

				if (methodName == null) {
					sb.append(String.format("callstatic ???, %d", instruction.getArgCount().value()));
				} else {
					sb.append(String.format("callstatic %s, %d", instruction.getArgCount().value()));
				}
			}

			@Override
			protected void visit(final AS3Callsuper instruction) {
				addMultinameInteger(sb, "callsuper", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Callsupervoid instruction) {
				addMultinameInteger(sb, "callsupervoid", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Checkfilter instruction) {
				add(sb, "checkfilter");
			}

			@Override
			protected void visit(final AS3Coerce instruction) {
				addMultiname(sb, "coerce", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Coercea instruction) {
				add(sb, "coerce_a");
			}

			@Override
			protected void visit(final AS3Coerces instruction) {
				add(sb, "coerce_s");
			}

			@Override
			protected void visit(final AS3Construct instruction) {
				add(sb, "construct", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Constructprop instruction) {
				addMultinameInteger(sb, "constructprop", instruction.getIndex().value(), instruction.getArgCount().value(), code);
			}

			@Override
			protected void visit(final AS3Constructsuper instruction) {
				add(sb, "constructsuper", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Convertb instruction) {
				add(sb, "convert_b");
			}

			@Override
			protected void visit(final AS3Convertd instruction) {
				add(sb, "convert_d");
			}

			@Override
			protected void visit(final AS3Converti instruction) {
				add(sb, "convert_i");
			}

			@Override
			protected void visit(final AS3Converto instruction) {
				add(sb, "convert_o");
			}

			@Override
			protected void visit(final AS3Converts instruction) {
				add(sb, "convert_s");
			}

			@Override
			protected void visit(final AS3Convertu instruction) {
				add(sb, "convert_u");
			}

			@Override
			protected void visit(final AS3Debug instruction) {

				final int index = instruction.getIndex().value();

				if (index < code.getData().getConstantPool().getStrings().size()) {
					final String constant = code.getData().getConstantPool().getStrings().get(index).getName().value();
					sb.append(String.format("debug %d, %s, %d, %d", instruction.getDebugType().value(), constant, instruction.getReg().value(), instruction.getExtra().value()));
				}
				else {
					sb.append(String.format("debug %d, ???, %d, %d", instruction.getDebugType().value(), instruction.getReg().value(), instruction.getExtra().value()));
				}
			}

			@Override
			protected void visit(final AS3Debugfile instruction) {
				addString(sb, "debugfile", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Debugline instruction) {
				add(sb, "debugline", instruction.getLineNum().value());
			}

			@Override
			protected void visit(final AS3Declocal instruction) {
				add(sb, "declocal", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Declocali instruction) {
				add(sb, "declocal_i", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Decrement instruction) {
				add(sb, "decrement");
			}

			@Override
			protected void visit(final AS3Decrementi instruction) {
				add(sb, "decrement_i");
			}

			@Override
			protected void visit(final AS3Deleteproperty instruction) {
				addMultiname(sb, "deletproperty", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Divide instruction) {
				add(sb, "divide");
			}

			@Override
			protected void visit(final AS3Dup instruction) {
				add(sb, "dup");
			}

			@Override
			protected void visit(final AS3Dxns instruction) {
				addString(sb, "dxns", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Dxnslate instruction) {
				add(sb, "dxns_late");
			}

			@Override
			protected void visit(final AS3Equals instruction) {
				add(sb, "equals");
			}

			@Override
			protected void visit(final AS3Escxattr instruction) {
				add(sb, "escx_attr");
			}

			@Override
			protected void visit(final AS3Escxelem instruction) {
				add(sb, "escx_elem");
			}

			@Override
			protected void visit(final AS3Findproperty instruction) {
				addMultiname(sb, "findproperty", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Findpropstrict instruction) {
				addMultiname(sb, "findpropstrict", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Getdescendants instruction) {
				addMultiname(sb, "getdescendants", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Getglobalscope instruction) {
				add(sb, "getglobalscope");
			}

			@Override
			protected void visit(final AS3Getglobalslot instruction) {
				add(sb, "getglobalslot");
			}

			@Override
			protected void visit(final AS3Getlex instruction) {
				addMultiname(sb, "getlex", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Getlocal instruction) {
				add(sb, "getlocal", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Getlocal0 instruction) {
				add(sb, "getlocal_0");
			}

			@Override
			protected void visit(final AS3Getlocal1 instruction) {
				add(sb, "getlocal_1");
			}

			@Override
			protected void visit(final AS3Getlocal2 instruction) {
				add(sb, "getlocal_2");
			}

			@Override
			protected void visit(final AS3Getlocal3 instruction) {
				add(sb, "getlocal_3");
			}

			@Override
			protected void visit(final AS3Getproperty instruction) {
				addMultiname(sb, "getproperty", instruction.getIndex().value() ,code);
			}

			@Override
			protected void visit(final AS3Getscopeobject instruction) {
				add(sb, "getscopeobject", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Getslot instruction) {
				add(sb, "getslot", instruction.getSlotIndex().value());
			}

			@Override
			protected void visit(final AS3Getsuper instruction) {
				addMultiname(sb, "getsuper", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Greaterthan instruction) {
				add(sb, "greaterthan");
			}

			@Override
			protected void visit(final AS3Hasnext instruction) {
				add(sb, "hasnext");
			}

			@Override
			protected void visit(final AS3Hasnext2 instruction) {
				add(sb, "hasnext", instruction.getObjectReg().value(), instruction.getIndexReg().value());
			}

			@Override
			protected void visit(final AS3Ifeq instruction) {
				addIf(sb, "ifeq", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Iffalse instruction) {
				addIf(sb, "iffalse", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifge instruction) {
				addIf(sb, "ifge", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifgt instruction) {
				addIf(sb, "ifgt", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifle instruction) {
				addIf(sb, "ifle", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Iflt instruction) {
				addIf(sb, "iflt", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifne instruction) {
				addIf(sb, "ifne", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifnge instruction) {
				addIf(sb, "ifnge", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifngt instruction) {
				addIf(sb, "ifngt", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifnle instruction) {
				addIf(sb, "ifnle", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifnlt instruction) {
				addIf(sb, "ifnlt", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifstricteq instruction) {
				addIf(sb, "ifstricteq", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Ifstrictne instruction) {
				addIf(sb, "ifstrictne", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3Iftrue instruction) {
				addIf(sb, "iftrue", instruction.getBitPosition() / 8 + instruction.getBitLength() / 8 + instruction.getOffset().value() - firstOffset);
			}

			@Override
			protected void visit(final AS3In instruction) {
				add(sb, "in");
			}

			@Override
			protected void visit(final AS3Increment instruction) {
				add(sb, "increment");
			}

			@Override
			protected void visit(final AS3Incrementi instruction) {
				add(sb, "increment_i");
			}

			@Override
			protected void visit(final AS3Initproperty instruction) {
				addMultiname(sb, "initproperty", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Inlocal instruction) {
				add(sb, "inlocal", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Inlocali instruction) {
				add(sb, "inlocal_i", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Instanceof instruction) {
				add(sb, "instanceof");
			}

			@Override
			protected void visit(final AS3Istype instruction) {
				addMultiname(sb, "istype", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Istypelate instruction) {
				add(sb, "istypelate");
			}

			@Override
			protected void visit(final AS3Jump instruction) {
				add(sb, "jump", instruction.getOffset().value());
			}

			@Override
			protected void visit(final AS3Kill instruction) {
				add(sb, "kill", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Label instruction) {
				add(sb, "label");
			}

			@Override
			protected void visit(final AS3Lessequals instruction) {
				add(sb, "lessequals");
			}

			@Override
			protected void visit(final AS3Lessthan instruction) {
				add(sb, "lessthan");
			}

			@Override
			protected void visit(final AS3Lookupswitch instruction) {
				// TODO Auto-generated method stub
			}

			@Override
			protected void visit(final AS3Lshift instruction) {
				add(sb, "lshift");
			}

			@Override
			protected void visit(final AS3Modulo instruction) {
				add(sb, "modulo");
			}

			@Override
			protected void visit(final AS3Multiply instruction) {
				add(sb, "multiply");
			}

			@Override
			protected void visit(final AS3Multiplyi instruction) {
				add(sb, "multiply_i");
			}

			@Override
			protected void visit(final AS3Negate instruction) {
				add(sb, "negate");
			}

			@Override
			protected void visit(final AS3Negatei instruction) {
				add(sb, "negate_i");
			}

			@Override
			protected void visit(final AS3Newactivation instruction) {
				add(sb, "newactivation");
			}

			@Override
			protected void visit(final AS3Newarray instruction) {
				add(sb, "newarray", instruction.getArgCount().value());
			}

			@Override
			protected void visit(final AS3Newcatch instruction) {
				add(sb, "newcatch", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Newclass instruction) {
				add(sb, "newclass", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Newfunction instruction) {
				add(sb, "newfunction", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Newobject instruction) {
				add(sb, "newobject", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Nextname instruction) {
				add(sb, "nextname");
			}

			@Override
			protected void visit(final AS3Nextvalue instruction) {
				add(sb, "nextvalue");
			}

			@Override
			protected void visit(final AS3Nop instruction) {
				add(sb, "nop");
			}

			@Override
			protected void visit(final AS3Not instruction) {
				add(sb, "not");
			}

			@Override
			protected void visit(final AS3Pop instruction) {
				add(sb, "pop");
			}

			@Override
			protected void visit(final AS3Popscope instruction) {
				add(sb, "popscope");
			}

			@Override
			protected void visit(final AS3Pushbyte instruction) {
				add(sb, "pushbyte", instruction.getByteValue().value());
			}

			@Override
			protected void visit(final AS3Pushdouble instruction) {
				addDouble(sb, "pushdouble", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Pushfalse instruction) {
				add(sb, "pushfalse");
			}

			@Override
			protected void visit(final AS3Pushint instruction) {
				addInteger(sb, "pushint", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Pushnamespace instruction) {
				addNamespace(sb, "pushnamespace", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Pushnan instruction) {
				add(sb, "pushnan");
			}

			@Override
			protected void visit(final AS3Pushnull instruction) {
				add(sb, "pushnull");
			}

			@Override
			protected void visit(final AS3Pushscope instruction) {
				add(sb, "pushscope");
			}

			@Override
			protected void visit(final AS3Pushshort instruction) {
				add(sb, "pushshort", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Pushstring instruction) {
				addString(sb, "pushstring", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Pushtrue instruction) {
				add(sb, "pushtrue");
			}

			@Override
			protected void visit(final AS3Pushuint instruction) {
				addUInteger(sb, "pushuint", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Pushundefined instruction) {
				add(sb, "pushundefined");
			}

			@Override
			protected void visit(final AS3Pushwith instruction) {
				add(sb, "pushwith");
			}

			@Override
			protected void visit(final AS3Returnvalue instruction) {
				add(sb, "returnvalue");
			}

			@Override
			protected void visit(final AS3Returnvoid instruction) {
				add(sb, "returnvoid");
			}

			@Override
			protected void visit(final AS3Rshift instruction) {
				add(sb, "rshift");
			}

			@Override
			protected void visit(final AS3Setglobalslot instruction) {
				add(sb, "setglobalslot", instruction.getSlotIndex().value());
			}

			@Override
			protected void visit(final AS3Setlocal instruction) {
				add(sb, "setlocal", instruction.getIndex().value());
			}

			@Override
			protected void visit(final AS3Setlocal0 instruction) {
				add(sb, "setlocal_0");
			}

			@Override
			protected void visit(final AS3Setlocal1 instruction) {
				add(sb, "setlocal_1");
			}

			@Override
			protected void visit(final AS3Setlocal2 instruction) {
				add(sb, "setlocal_2");
			}

			@Override
			protected void visit(final AS3Setlocal3 instruction) {
				add(sb, "setlocal_3");
			}

			@Override
			protected void visit(final AS3Setproperty instruction) {
				addMultiname(sb, "setproperty", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Setslot instruction) {
				add(sb, "setslot", instruction.getSlotIndex().value());
			}

			@Override
			protected void visit(final AS3Setsuper instruction) {
				addMultiname(sb, "setsuper", instruction.getIndex().value(), code);
			}

			@Override
			protected void visit(final AS3Strictequals instruction) {
				add(sb, "strictequals");
			}

			@Override
			protected void visit(final AS3Subtract instruction) {
				add(sb, "subtract");
			}

			@Override
			protected void visit(final AS3Subtracti instruction) {
				add(sb, "subtract_i");
			}

			@Override
			protected void visit(final AS3Swap instruction) {
				add(sb, "swap");
			}

			@Override
			protected void visit(final AS3Throw instruction) {
				add(sb, "throw");
			}

			@Override
			protected void visit(final AS3Typeof instruction) {
				add(sb, "typeof");
			}

			@Override
			protected void visit(final AS3UnknownInstruction instruction) {
				add(sb, "unknown");
			}

			@Override
			protected void visit(final AS3Urshift instruction) {
				add(sb, "urshift");
			}
		}.visit(instruction);
	}

	/**
	 * Resolves and adds an integer value to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param integerIndex The integer index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addInteger(final StringBuilder sb, final String mnemonic, final int integerIndex, final ResolvedCode code) {

		final Long integer = code.resolveInteger(integerIndex - 1);

		sb.append(mnemonic);
		sb.append(" ");

		if (integer == null) {
			sb.append(String.format("??? [0x%08X]", integerIndex));
		}
		else {
			sb.append(String.format("%d [0x%08X]", integer, integerIndex));
		}
	}

	/**
	 * Adds a method to the output.
	 * 
	 * @param code The code the method belongs to.
	 * @param resolvedMethod The method to add to the output.
	 * @param className The name of the enclosing class the method belongs to.
	 * @param sb The string builder the output is appended to.
	 * 
	 * @return True, if the method has code. False, if the method is just a declaration.
	 */
	private static boolean addMethod(final ResolvedCode code, final ResolvedMethod resolvedMethod, final String className, final StringBuilder sb) {
		sb.append("\t");
		final String flattenedReturnType = ActionScript3Helpers.flattenNamespaceName(resolvedMethod.getReturnType());
		sb.append(flattenedReturnType);

		if (!flattenedReturnType.isEmpty()) {
			// This path is taken for all methods but constructors.
			sb.append(" ");
		}

		final String functionName = ActionScript3Helpers.flattenNamespaceName(resolvedMethod.getName());

		if (functionName.startsWith(className)) {
			// To make code more readable, strip fully qualified type
			// information.
			sb.append(functionName.substring(className.length() + 1));
		}
		else {
			sb.append(functionName);
		}

		sb.append("(");

		// Print the method arguments.
		for (final String[] argument : resolvedMethod.getArguments()) {

			if (argument != resolvedMethod.getArguments().get(0)) {
				sb.append(", ");
			}

			sb.append(ActionScript3Helpers.flattenNamespaceName(argument));
		}

		sb.append(")");

		// Print the code.
		final AS3Code methodCode = resolvedMethod.getCode();

		if (methodCode == null) {
			sb.append(";\n");
			return false;
		}
		else {
			sb.append("\n");
			sb.append("\t{");
			sb.append("\n");
			sb.append(getCodeText(code, methodCode, "\t\t"));
			sb.append("\t}\n");
			return true;
		}
	}

	/**
	 * Resolves and adds an multiname instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param multiName The multiname index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addMultiname(final StringBuilder sb, final String mnemonic, final int multiName, final ResolvedCode code) {

		final String[] multinameString = code.resolveMultiname(multiName);

		sb.append(mnemonic);
		sb.append(" ");

		if (multinameString == null) {
			sb.append(String.format("??? [0x%08X]", multiName));
		}
		else {
			sb.append(String.format("%s [0x%08X]", ActionScript3Helpers.flattenNamespaceName(multinameString), multiName));
		}
	}

	/**
	 * Resolves and adds a multiname + integer instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param multiName The multiname index.
	 * @param value The integer value to add.
	 * @param code The code the instruction belongs to.
	 */
	private static void addMultinameInteger(final StringBuilder sb, final String mnemonic, final int multiName, final int value, final ResolvedCode code) {

		final String[] multinameString = code.resolveMultiname(multiName);

		sb.append(mnemonic);
		sb.append(" ");

		if (multinameString == null) {
			sb.append(String.format("??? [0x%08X], %d", multiName, value));
		}
		else {
			sb.append(String.format("%s [0x%08X], %d", ActionScript3Helpers.flattenNamespaceName(multinameString), multiName, value));
		}
	}

	/**
	 * Resolves and adds a namespace instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param namespace The namespace index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addNamespace(final StringBuilder sb, final String mnemonic, final int namespace, final ResolvedCode code) {

		final String namespaceString = code.resolveNamespace(namespace);

		sb.append(mnemonic);
		sb.append(" ");

		if (namespaceString == null) {
			sb.append(String.format("??? [0x%08X]", namespace));
		}
		else {
			sb.append(String.format("\"%s\" [0x%08X]", namespaceString, namespace));
		}
	}

	/**
	 * Resolves and adds a string value instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param stringIndex The string index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addString(final StringBuilder sb, final String mnemonic, final int stringIndex, final ResolvedCode code) {

		final String string = code.resolveString(stringIndex - 1);

		sb.append(mnemonic);
		sb.append(" ");

		if (string == null) {
			sb.append(String.format("??? [0x%08X]", stringIndex));
		}
		else {
			sb.append(String.format("\"%s\" [0x%08X]", string, stringIndex));
		}
	}

	/**
	 * Resolves and adds an unsigned integer value instruction to the output.
	 * 
	 * @param sb The string builder the output is appended to.
	 * @param mnemonic The mnemonic of the instruction.
	 * @param uintIndex The unsigned integer index.
	 * @param code The code the instruction belongs to.
	 */
	private static void addUInteger(final StringBuilder sb, final String mnemonic, final int uintIndex, final ResolvedCode code) {

		final Long integer = code.resolveUInteger(uintIndex - 1);

		sb.append(mnemonic);
		sb.append(" ");

		if (integer == null) {
			sb.append(String.format("??? [0x%08X]", uintIndex));
		}
		else {
			sb.append(String.format("%d [0x%08X]", integer, uintIndex));
		}
	}

	/**
	 * Generates a printable string that represents the given ActionScript 3 code.
	 * 
	 * @param resolvedCode The ActionScript 3 code to turn into a string.
	 * @param code The raw ActionScript 3 code.
	 * @param prefix The prefix to write before every printed line.
	 * 
	 * @return The generated ActionScript 3 code string.
	 */
	private static String getCodeText(final ResolvedCode resolvedCode, final AS3Code code, final String prefix) {

		if (code.getInstructions().size() == 0) {
			return "";
		}

		final StringBuilder sb = new StringBuilder();

		final AS3Instruction firstInstruction = code.getInstructions().get(0);

		final int firstOffset = firstInstruction.getBitPosition();

		for (final AS3Instruction instruction : code.getInstructions()) {

			final int absoluteOffset = instruction.getBitPosition() / 8;
			final int relativeOffset = absoluteOffset - firstOffset  / 8;
			sb.append(prefix);
			sb.append(String.format("%08X %08X  ", absoluteOffset, relativeOffset));

			addInstructionText(sb, instruction, resolvedCode, firstOffset / 8);

			sb.append('\n');
		}

		return sb.toString();
	}

	/**
	 * Determines the method name of a method.
	 * 
	 * @param methodIndex The index of the method whose name is returned.
	 * @param code The resolved code the method belongs to.
	 * 
	 * @return The method name or null if the method name could not be resolved.
	 */
	private static String getMethodName(final int methodIndex, final ResolvedCode code) {
		if (methodIndex >= code.getData().getMethodInfos().size()) {
			return null;
		}

		final MethodInfo method = code.getData().getMethodInfos().get(methodIndex);

		final int nameIndex = method.getName().value();

		if (nameIndex >= code.getData().getConstantPool().getStrings().size()) {
			return null;
		}
		else {
			return code.getData().getConstantPool().getStrings().get(nameIndex).getName().value();
		}
	}

	/**
	 * Generates a printable string that represents all code in a given
	 * resolved ActionScript 3 code snippet.
	 * 
	 * @param code The resolved code to display.
	 * 
	 * @return The generated ActionScript 3 code string.
	 */
	public static String getCodeText(final ResolvedCode code) {
		final StringBuilder sb = new StringBuilder();

		for (final ResolvedClass resolvedClass : code.getClasses()) {

			// Start out with the class definition.
			addClassHeader(resolvedClass, sb);

			boolean hadCode = false;

			// Start preparing all the methods for printing. Add the instance
			// constructor and the class constructor for printing.
			final ResolvedMethod staticConstructor = resolvedClass.getStaticConstructor();
			final ResolvedMethod constructor = resolvedClass.getConstructor();

			final List<ResolvedMethod> resolvedMethods = resolvedClass.getMethods();

			resolvedMethods.add(0, constructor);

			if (staticConstructor.getCode() != null) {
				// Only add the static constructor if it actually has code.
				resolvedMethods.add(0, staticConstructor);
			}

			final String className = ActionScript3Helpers.flattenNamespaceName(resolvedClass.getName());

			// Print the individual methods now.
			for (final ResolvedMethod resolvedMethod : resolvedMethods) {

				if (resolvedMethod != resolvedMethods.get(0)) {
					if (hadCode || resolvedMethod.getCode() != null) {
						sb.append("\n");
					}
				}

				hadCode = addMethod(code, resolvedMethod, className, sb);
			}

			addClassFooter(sb);
		}

		return sb.toString();
	}
}