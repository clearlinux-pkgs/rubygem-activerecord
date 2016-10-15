#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-activerecord
Version  : 5.0.0.1
Release  : 14
URL      : https://rubygems.org/downloads/activerecord-5.0.0.1.gem
Source0  : https://rubygems.org/downloads/activerecord-5.0.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
= Active Record -- Object-relational mapping in Rails
Active Record connects classes to relational database tables to establish an
almost zero-configuration persistence layer for applications. The library
provides a base class that, when subclassed, sets up a mapping between the new
class and an existing table in the database. In the context of an application,
these classes are commonly referred to as *models*. Models can also be
connected to other models; this is done by defining *associations*.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n activerecord-5.0.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-activerecord.gemspec

%build
export LANG=C
gem build rubygem-activerecord.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
activerecord-5.0.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/activerecord-5.0.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/examples/performance.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/examples/simple.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/aggregations.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/association_relation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/alias_tracker.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/association_scope.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/belongs_to_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/belongs_to_polymorphic_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/belongs_to.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/collection_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/has_and_belongs_to_many.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/has_many.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/has_one.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/builder/singular_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/collection_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/collection_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/foreign_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/has_many_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/has_many_through_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/has_one_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/has_one_through_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/join_dependency.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/join_dependency/join_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/join_dependency/join_base.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/join_dependency/join_part.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/belongs_to.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/collection_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/has_many.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/has_many_through.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/has_one.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/has_one_through.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/singular_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/preloader/through_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/singular_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/associations/through_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute/user_provided_default.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_assignment.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_decorators.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/before_type_cast.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/dirty.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/primary_key.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/query.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/read.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/serialization.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/time_zone_conversion.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_methods/write.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_mutation_tracker.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attribute_set/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/autosave_association.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/coders/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/coders/yaml_column.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/collection_cache_key.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/connection_pool.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/database_limits.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/database_statements.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/query_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/quoting.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/savepoints.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/schema_creation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/schema_definitions.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/schema_dumper.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/schema_statements.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract/transaction.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/abstract_mysql_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/column.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/connection_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/determine_if_preparable_visitor.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/column.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/database_statements.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/explain_pretty_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/quoting.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/schema_creation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/schema_definitions.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/schema_dumper.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql/type_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/mysql2_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/column.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/database_statements.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/explain_pretty_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/array.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/bit.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/bit_varying.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/bytea.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/cidr.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/date_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/decimal.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/enum.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/hstore.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/inet.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/jsonb.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/money.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/point.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/rails_5_1_point.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/range.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/specialized_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/type_map_initializer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/uuid.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/vector.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/oid/xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/quoting.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/referential_integrity.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/schema_definitions.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/schema_dumper.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/schema_statements.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/type_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql/utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/postgresql_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/schema_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/sql_type_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/sqlite3/explain_pretty_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/sqlite3/quoting.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/sqlite3/schema_creation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/sqlite3_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_adapters/statement_pool.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/connection_handling.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/counter_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/dynamic_matchers.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/enum.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/explain.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/explain_registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/explain_subscriber.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/fixture_set/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/fixtures.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/gem_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/inheritance.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/integration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/internal_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/legacy_yaml_adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/locale/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/locking/optimistic.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/locking/pessimistic.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/log_subscriber.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/migration/command_recorder.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/migration/compatibility.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/migration/join_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/model_schema.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/nested_attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/no_touching.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/null_relation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/persistence.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/query_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/querying.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/railties/console_sandbox.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/railties/controller_runtime.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/railties/databases.rake
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/railties/jdbcmysql_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/readonly_attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/reflection.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/batches.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/batches/batch_enumerator.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/calculations.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/delegation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/finder_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/from_clause.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/merger.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/array_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/association_query_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/base_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/basic_object_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/class_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/polymorphic_array_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/range_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/predicate_builder/relation_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/query_attribute.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/query_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/record_fetch_warning.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/spawn_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/where_clause.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/relation/where_clause_factory.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/result.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/runtime_registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/sanitization.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/schema.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/schema_dumper.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/schema_migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/scoping.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/scoping/default.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/scoping/named.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/secure_token.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/serialization.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/statement_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/store.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/suppressor.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/table_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/tasks/database_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/tasks/mysql_database_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/tasks/postgresql_database_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/tasks/sqlite_database_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/timestamp.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/touch_later.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/transactions.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/translation.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/adapter_specific_registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/date.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/date_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/hash_lookup_type_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/internal/abstract_json.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/internal/timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/serialized.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/time.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type/type_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type_caster.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type_caster/connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/type_caster/map.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations/absence.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations/associated.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations/length.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations/presence.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/validations/uniqueness.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/active_record/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/migration/migration_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/migration/templates/create_table_migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/migration/templates/migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/model/model_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/model/templates/application_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/model/templates/model.rb
/usr/lib64/ruby/gems/2.3.0/gems/activerecord-5.0.0.1/lib/rails/generators/active_record/model/templates/module.rb
/usr/lib64/ruby/gems/2.3.0/specifications/activerecord-5.0.0.1.gemspec
