## First Principles

### Study Before Writing
- **ALWAYS examine existing code first** - Spend time understanding current patterns before writing a single line
- **Never assume conventions** - What works in one codebase may not apply to another
- **Look for implicit patterns** - Sometimes the most important rules aren't written down

### Pattern Recognition Priority
1. **Naming conventions** - How are variables, functions, classes, and files named?
2. **File organization** - Where do similar files live? How are they grouped?
3. **Code style** - Spacing, brackets, quotes, semicolons, indentation
4. **Architecture patterns** - MVC? Component-based? Functional? Service-oriented?

## Naming Convention Analysis

### Detect and Follow
- **Variables**: camelCase? snake_case? PascalCase? 
- **Functions/Methods**: getUser? get_user? GetUser? fetchUser? retrieveUser?
- **Directories**: components/ or Components/? utils/ or helpers/ or lib/?
- **Constants**: UPPER_SNAKE_CASE? ALL_CAPS? Config.CONSTANT?

### Semantic Patterns
- **Boolean naming**: isActive? hasPermission? shouldRender? active? canEdit?
- **Collection naming**: users (plural)? userList? userArray? usersData?
- **Event handlers**: onClick? handleClick? clickHandler? onUserClick?
- **Async functions**: fetchUser? getUserAsync? loadUser? getUser?

## Code Organization Principles

### Observe Structure Before Creating
- **Check if similar files exist** - Never create a new pattern if one already exists
- **Maintain locality** - Put new code near related existing code
- **Respect boundaries** - Don't mix layers (e.g., database code in UI components)

### File Placement Rules
1. **Find similar functionality** - Where do similar features live?
2. **Check import patterns** - How do other files import similar utilities?
3. **Follow depth patterns** - How deep is the directory nesting?
4. **Respect separation** - Keep tests, docs, and code in established locations

## Writing Style Consistency

### Language-Agnostic Patterns
- **Line length** - Are lines kept short? What's the apparent limit?
- **Function size** - How large are typical functions? When are they split?
- **Comment style** - Block comments? Inline? JSDoc? Docstrings?
- **Whitespace** - Blank lines between functions? Around blocks?

### Error Handling Patterns
- **Try-catch vs. error returns** - Which pattern does the codebase prefer?
- **Error messages** - How descriptive? What format? User-facing or technical?
- **Validation location** - At entry points? Throughout? Dedicated layer?

## Quality Standards

### Before Writing Any Code
1. **Find 3 similar examples** - Never write without reference
2. **Identify the why** - Understand why existing patterns exist
3. **Check for anti-patterns** - What does the codebase actively avoid?

### The Rule of Least Surprise
- **Be predictable** - New code should feel like it belongs
- **Avoid novelty** - Don't introduce new patterns without strong justification
- **Match complexity** - Simple codebases deserve simple solutions

## Refactoring Approach

### When to Refactor
- **Only refactor what you touch** - Don't refactor unrelated code
- **Preserve existing patterns** - Unless explicitly asked to modernize
- **Incremental changes** - Small, testable improvements

### When NOT to Refactor
- **Working code you're not modifying** - If it ain't broke...
- **Without understanding context** - That "bad" code might have good reasons
- **Style preferences** - Your preferred style < codebase consistency

## Documentation Principles

### Match Existing Documentation
- **Format** - README.md? docs/? Wiki? Inline comments only?
- **Detail level** - Sparse? Comprehensive? Just the essentials?
- **Tone** - Technical? Friendly? Formal?
- **Examples** - Are examples provided? What format?

### Comment Philosophy
- **Match density** - If existing code has few comments, don't over-comment
- **Match style** - Single-line? Multi-line? Above or beside code?
- **Match content** - Do comments explain why or what? Business logic or technical?

## Technology-Agnostic Best Practices

### Dependency Management
- **Check before adding** - Is there already a solution in the codebase?
- **Match versions** - Use consistent versioning strategies
- **Respect the stack** - Don't add React to a Vue project

### Testing Patterns
- **Match test structure** - Unit? Integration? E2E? What's the balance?
- **Follow naming** - test_user_creation? testUserCreation? "should create user"?
- **Respect coverage** - Match the existing level of test coverage

## The Golden Rules

### 1. Observation Over Assumption
Never assume you know the "right" way. The right way is the way the codebase already does it.

### 2. Consistency Over Correctness
A consistently "wrong" pattern is better than mixed "right" and "wrong" patterns.

### 3. Evolution Over Revolution
Improve gradually. Revolutionary changes should be explicit requests, not suggestions.

### 4. Context is King
What's "best practice" in one codebase may be an anti-pattern in another. Always prioritize local context.

### 5. When in Doubt, Ask
If you can't find a pattern to follow, ask before inventing one. Show examples of what you found and explain your uncertainty.

## Final Checklist

Before submitting any code:
- [ ] Does it look like it was written by the same person who wrote the rest?
- [ ] Could someone guess which file is yours? (They shouldn't be able to)
- [ ] Did you introduce any new patterns? (You probably shouldn't have)
- [ ] Is your code surprising in any way? (It shouldn't be)
- [ ] Would a maintainer thank you or curse you? (Aim for thanks)## First Principles
