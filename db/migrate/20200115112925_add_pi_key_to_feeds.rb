class AddPiKeyToFeeds < ActiveRecord::Migration[5.1]
  def change
    add_column :feeds, :pi_key, :string
    add_index :feeds, :pi_key, unique: true
  end
end
