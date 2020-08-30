# Ruby and Rails Interview Questions
These questions are collected from the Internet.

## References

- How to Interview Your Ruby on Rails Developer
  https://rubygarage.org/blog/how-to-interview-your-ruby-on-rails-developer
- 53 Ruby on Rails Interview Questions and Answers
  https://medium.com/better-programming/53-ruby-on-rails-interview-questions-and-answers-eb99eed1aeb7
- Top 53 Ruby on Rails Interview Questions & Answers
  https://career.guru99.com/top-34-ruby-on-rail-interview-questions/
- Ruby on Rails Interview Questions for Experienced
  https://blog.interviewmocha.com/ruby-on-rails-interview-questions-for-experienced

## Ruby

### Language and OOP

- What is a class?

- What is the difference between a class and a module?
  A class has attributes and methods. You can create an instance of a class.
  A module is just a collection of methods and constants, which you can mixin with another module or class.

- What is an object?

- How would you declare and use a constructor in Ruby?
  A constructor is defined via an initialize method which is called when a new instance of a class is initialized. Defining this method is not required. It’s often used to provide attribute values on new instances.

- How would you create getter and setter methods in Ruby?

- Describe the difference between class and instance variables?

  - Ruby Instance variable begins with — **@**
  - Ruby Class variables begin with — **@@**
  - Ruby Global variables begin with — **$**

- What is the difference between class methods and instance methods?
  Class methods are available on classes, and instance methods are available on instances (of course).They are typically used for different purposes.
  Class methods are denoted by `def self.method_name`.

- What are the three levels of method access control for classes and what do they signify?

  - `public`: Any object can call this method.
  - `protected`: Only the class that defined the method and its subclasses can call the method.
  - `private`: Only the object itself can call this method.

- What does "**self**" mean?
  Use self when defining and calling class methods.
  In a class, self refers to the current class so it’s required when a class method calls another class method.
  self.class.method is required when an instance calls a class method.

- Explain how (almost) everything is an object in Ruby.

- Explain what singleton methods are. What is Eigenclass in Ruby?

- Describe Ruby method lookup path.

- Describe available Ruby callbacks. How can we use them in practice?

- What is a block in Ruby?
  A block is the code between two braces, `{…}`, or between `do` and `end`. You’re passing a block every time you call `.each`.

  Blocks have their own scope and variables only defined inside a block are not accessible outside. But variables defined outside a block can be modified inside a block.

  ```ruby
  {|x| puts x} # a block
  ```

- What is the difference between Proc and lambda?
  Both procs and lambdas are stored blocks but syntax and behavior differs slightly.
  A lambda returns from itself but a proc returns from the method it’s inside.

  ```ruby
  def method_proc
    thing  = Proc.new { return 1}
    thing.call
    return 2
  end
  def method_lambda
    thing  = lambda { return 1}
    thing.call
    return 2
  end
  puts method_proc # => 1
  puts method_lambda # => 2
  ```

- What is yield in Ruby?
  yield accesses a block passed to a method. It’s typically used in layout files in a Rails application.

  ```ruby
  def puts_stuff
   puts 'first line'
   yield if block_given?
   puts 'third line'
   yield if block_given?
  end
  puts_stuff { puts 'its me' }
  # => first line
  # => its me 
  # => third line
  # => its me
  ```

- What is the difference between Hash and JSON?
  `Hash` is a Ruby class, a collection of key/value pairs that allows accessing values by keys.

  `JSON` is a string in a specific format for sending data.

- What is the splat operator?
  Splat is used when you don’t want to specify the number of arguments passed to a method in advance. Ruby has two splat operators, the single splat and double splat.
  The single splat works as you’d expect:

  ```ruby
  def do_sth(*input)
    input.each {|x| puts x }
  end
  do_sth(3,4,5)
  # => 3
  # => 4
  # => 5
  ```

  The double splat is like the single splat but it takes key/values as arguments.

  ```ruby
  def do_sth(**input)
    input.each {|k,v| puts v }
  end
  do_sth('a':3, 'b':4, 'c':5)
  # => 3
  # => 4
  # => 5
  ```

- What is [SOLID Principles](https://itnext.io/solid-principles-explanation-and-examples-715b975dcad4) ?

- Does Ruby allow multiple inheritances?
  Ruby does not allow inheriting from more than one parent class, but it does allow module mixins with include and extend.

- What is the difference between include and extend?
  Both are mixins that allow injecting code from another module.
  
  But `include` allows accessing that code via class methods, while `extend` allows accessing that code via instance methods.
  
  ```ruby
  module Greetings
    def hello
      puts 'hello'
    end
  end
  module Farewells
    def bye
      puts 'bye'
     end
  end
  class Conversation
    extend Greetings
    include Farewells
  end
  # class method
  Conversation.hello
  # => hello
  # instance method
  c = Conversation.new
  c.bye
  # => bye
  ```

- What is the difference between load and require?
  load runs another file, even if it’s already in memory.
  require will only run another file once, no matter how many times you require it.
  
- What is the purpose of load, auto_load, and require_relative in Ruby?
  
- What is the difference between select, map, and collect?
  
  - `select`: Is used to grab a subset of a collection. Calling `.select!` with a bang mutates the original collection.
    ```ruby
    i = [1,2,3,4,5]
    i.select {|x| x % 2 == 0}
    # => [2, 4]
  ```
  
  - `map`: Performs an action on each element of a collection and outputs an updated collection. Calling `.map!` with a bang mutates the original collection.
  
    ```ruby
    i = [1,2,3,4,5]
    i.map {|x| x+1}
    # => [2,3,4,5,6]
    ```
    
  - `collect`: Is an alias of `.map` and does the same thing.
  
- Mention what the difference is between false and nil in Ruby?
  False indicates a Boolean datatype, while Nil is not a data type, it have an object_id 4.

- Mention what is the difference between String and Symbol?
  They both act in the same way only they differ in their behaviors which are opposite to each other. The difference lies in the object_id, memory and process tune when they are used together. Symbol belongs to the category of immutable objects whereas Strings are considered as mutable objects.

  - In Ruby string is mutable but a Symbol is immutable
  - Only one copy of the symbol requires to be created
  - Symbols are often used as the corresponding to enums in Ruby

### Business Applications

- What is Rack?
  Rack is an API sitting between the web server and Rails. It allows plugging in and swapping frameworks like Rails with Sinatra, or web servers like Unicorn with Puma.
- Explain the Rack application interface.
- Write a simple Rack application.
- How does Rack middleware works?

### Gem

- What is RubyGems? How does it work?
- How can you build your own Ruby gem?
- Explain the structure of a Ruby gem.
- Can you give me some examples of your favorite gems besides Ruby on Rails?
  [57 Best Ruby Gems We Use at RubyGarage](https://rubygarage.org/blog/best-ruby-gems-we-use)

## Rails and Web development

- What is ActiveJob? When should we use it?
  Allows creating background jobs and queuing them on a variety of back ends like Delayed::Job or Sidekiq.
  It’s typically used to execute code that doesn’t need to be executed in the main web thread. A common use case is sending notification emails to users.

- What is Asset Pipeline?
  It’s a framework that prepares JavaScript and CSS for the browser.

- Explain the difference between Page, Action, Fragment, Low-Level, SQL caching types.

- What is a Rails engine?

- What are some Rails design patterns you’ve used?
  [7 Design Patterns to Refactor MVC Components in Rails](https://www.sitepoint.com/7-design-patterns-to-refactor-mvc-components-in-rails/)
  
- What are initializers in Rails?

  Initializers hold configuration logic and only run when an app is booted. This means the Rails server needs to be restarted if initializers are changed. They exist in the `/config/initializers` directory.
  
- What is Spring?
  Spring is an application preloader. It keeps the application running in the background so booting is not required any time you run a migration or rake task.

- Mention what is Rails Migration?
  Rails Migration enables Ruby to make changes to the database schema, making it possible to use a version control system to leave things synchronized with the actual code.

- Mention what is the function of garbage collection in Ruby on Rails?
  The functions of garbage collection in Ruby on Rails includes

  - It enables the removal of the pointer values which is left behind when the execution of the program ends
  - It frees the programmer from tracking the object that is being created dynamically on runtime
  - It gives the advantage of removing the inaccessible objects from the memory, and allows other processes to use the memory

### Routing, Controllers, and Views

- Provide an example of RESTful routing and controller.
- Describe CRUD verbs and actions.
- How should you test routes?
- How should you use filters in controllers?
- What are Strong Parameters?
- What do we need to test in controllers?
- How should you use **content_for** and **yield**?
  [Rails what is the difference between content_for and yield?](https://stackoverflow.com/questions/13150983/rails-what-is-the-difference-between-content-for-and-yield)
  **content_for** allows defining and rendering content in views. This is useful for defining content in one place and rendering it in many.
- How should you use nested layouts?
- What logic goes into a helper?
  Helper logic should support views only.
  A good candidate for a helper is date formatting logic required in several different views.

### Active Record

- Explain the Active Record pattern.

- What is Object-Relational Mapping?
  Active Record is an ORM (object-relational mapping) that maps models to database tables. It simplifies setting up an app because we no longer have to write SQL directly to load, save, or delete objects.
  It also provides some protection against SQL injection.
  
- Describe Active Record conventions.

- Explain the Migrations mechanism.

- Describe types of associations in Active Record.

- What is Scopes? How should you use it?
  A scope is ActiveRecord query logic that you can define inside a model and call elsewhere.
  Defining a scope can be useful rather than duplicating the same logic in many places in the app.

  ```ruby
  # an example scope
  class Post
    scope :active_posts, -> { where(active:true) }
  end
  ```

- Explain the difference between optimistic and pessimistic locking.

- What is the difference between count, length, and size?
  - count: Executes an SQL query to count the number of records. This is useful if the number of records may have changed in the DB vs. memory.
  - length: Returns the number of items in a collection in memory. It’s lighter weight than count because no database transaction is performed. It can also be used to count characters in a string.
  - size: This is an alias for length and does the same thing.
  
- What is the difference between delete and destroy?
  - delete: Deletes a record.
  - destroy: Deletes a record and executes callbacks.
  
- What is the difference between find, find_by, and where in ActiveRecord?

  - find: Takes a single argument and looks up the record where the primary key matches that argument.
  - find_by: Takes key/values and returns the first matching record.
  - where: Takes key/values and returns a collection of matching records. Or an empty collection if there are no matches.

- Mention what is the difference between the Observers and Callbacks in Ruby on Rails?

  - **Rails Observers:** Observers is same as Callback, but it is used when method is not directly associated to object lifecycle. Also, the observer lives longer, and it can be detached or attached at any time. For example, displaying values from a model in the UI and updating model from user input.
  - **Rails Callback:** Callbacks are methods, which can be called at certain moments of an object’s life cycle for example it can be called when an object is validated, created, updated, deleted, A call back is short lived. For example, running a thread and giving a call-back that is called when thread terminates

### Security

[Ruby on Rails Web Application Vulnerabilities: How to Make Your App Secure](https://rubygarage.org/blog/ruby-on-rails-web-application-vulnerabilities-how-to-make-your-app-secure)

- Explain what is a sessions mechanism. How does it work?
- Describe cross-site request forgery, cross-site scripting, session hijacking, and session fixation attacks.
- What is the difference between SQL Injection and CSS Injection?
- How should you store secure data such as a password?
- Why do we need to use HTTPS instead of HTTP?

### Testing

- What is unit testing (in classical terms)?
- What is the primary technique for writing a test?
- What are your favorite tools for writing unit tests?
- What are your favorite tools for writing feature tests?

### Refactoring

- What is a code smell?
- What are your favorite tools to find code smells and potential bugs?
- Why should you avoid fat controllers?
- Why should you avoid fat models?
- What is the meaning of “Fat models, skinny controllers”?
  Business logic should exist in models, not controllers. This makes logic easier to unit test and is more re-usable.
  Controllers are merely the hands that pass information between views and models.
  This is generally given as advice to new Rails developers. It’s not actually recommended, particularly in large apps.
- What is the meaning of “skinny controllers, skinny models”?
  As a codebase grows, fat models get out of hand, start doing too many things and become unmanageable. Models should handle persistence without being bloated with logic.
  Models can be made skinnier by keeping the single responsibility principle in mind and moving logic out of models, and into other design patterns like service objects.
- Explain extract Value, Service, Form, View, Query, and Policy Objects techniques.


# Ruby on Rails Developer Skills

## Entry Level

Create and setup a Rails environment

Use generators to create models, controllers, and migrations

Create and use a migration to manage the database

Create a unit test using rspec/etc

Create a model and basic validations

Handle a GET request using a Controller, Model, and View

Handle a POST request using a Controller, Model, and View

Basic HTML, CSS and JavaScript

Basic GIT - clone, commit, push.

MYSQL

Linux Administration

Agile Methodology

##Mid-level

Setup and deploy a Rails App for production

Understand the Rails stack - callbacks, filters, plug-ins, engines, gems, rack

Understand and use Active Record associations

Understand and use scopes to define model abstractions

Define tests using Cucumber and rSpec

Understand and use Object Orientation

Understand and use Design Patterns (explain what they are, know some basic patterns)

Linux Administration

Agile Methodology

##Senior

Analyze and profile an application for performance and memory issues

Analyzes and profile an application for security issues

Understand database modeling and query analysis

Tune a production deployment (Passenger, Thin, Apache etc)

Understand and use Ruby metaprogramming

Mentoring skills

Communication skills

Planning and Estimation